import torch
import torch.nn as nn
import torch.nn.functional as F


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding, self).__init__()
        # 创建位置编码表
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        # 将位置编码与输入嵌入相加
        return x + self.pe[:x.size(0), :]

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super(MultiHeadAttention, self).__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads

        assert (
            self.head_dim * n_heads == d_model
        ), "Embedding size needs to be divisible by n_heads"

        self.values = nn.Linear(d_model, d_model, bias=False)
        self.keys = nn.Linear(d_model, d_model, bias=False)
        self.queries = nn.Linear(d_model, d_model, bias=False)
        self.fc_out = nn.Linear(d_model, d_model)

    def forward(self, values, keys, query, mask):
        N = query.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]

        # 分割成多个头
        values = values.reshape(N, value_len, self.n_heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.n_heads, self.head_dim)
        queries = query.reshape(N, query_len, self.n_heads, self.head_dim)

        values = self.values(values)
        keys = self.keys(keys)
        queries = self.queries(queries)

        # 缩放点积注意力
        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys]) / (self.d_model ** (1 / 2))

        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))

        attention = torch.softmax(energy, dim=3)

        out = torch.einsum("nhql,nlhd->nqhd", [attention, values]).reshape(
            N, query_len, self.d_model
        )

        out = self.fc_out(out)
        return out
