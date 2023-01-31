import pyupbit

access = "bTvS5mYsYAqdDIGHJppUfnu7ZygjfexEjStVexEB"          # 본인 값으로 변경
secret = "mWKciPM90Hj6fhEHwEoryndjxkhMr2L9wkExMofS"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

