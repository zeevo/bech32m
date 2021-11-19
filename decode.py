from segwit_addr import bech32_decode, CHARSET

hrp, data, spec = bech32_decode(
    "tb1p84x2ryuyfevgnlpnxt9f39gm7r68gwtvllxqe5w2n5ru00s9aquslzggwq"
)

print(hrp, data, spec)

# Possibly the pubkeyhash of a bech32m address
print("".join([CHARSET[a] for a in data]))
