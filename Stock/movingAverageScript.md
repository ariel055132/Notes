```
//@version=1
//@Author: adrian

study(title="7 Moving Averages", shorttitle="7MA", overlay=true)

sma1_length = input(10, minval=1, title="#1 SMA Length")
sma2_length = input(20, minval=1, title="#2 SMA Length")
sma3_length = input(50, minval=1, title="#3 SMA Length")
sma4_length = input(200, minval=1, title="#4 SMA Length")

ema1_length = input(20, minval=1, title="#1 EMA Length")
ema2_length = input(63, minval=1, title="#2 EMA Length")
ema3_length = input(150, minval=1, title="#3 EMA Length")

sma1_out = sma(close, sma1_length)
sma2_out = sma(close, sma2_length)
sma3_out = sma(close, sma3_length)
sma4_out = sma(close, sma4_length)

ema1_out = ema(close, ema1_length)
ema2_out = ema(close, ema2_length)
ema3_out = ema(close, ema3_length)

plot(sma1_out ? sma1_out: na, title="SMA1", color=#9e9d9d)
plot(sma2_out ? sma2_out: na, title="SMA2", color=#89d992)
plot(sma3_out ? sma3_out: na, title="SMA3", color=#5989f7)
plot(sma4_out ? sma4_out: na, title="SMA3", color=#f74068)

plot(ema1_out ? ema1_out: na, title="EMA1", color=#118207)
plot(ema2_out ? ema2_out: na, title="EMA2", color=#ee8ef5)
plot(ema3_out ? ema3_out: na, title="EMA3", color=#fcaf49)
```