# 策略
## Overview
1. 看大趨勢 (牛/熊，熊轉牛，牛轉熊)
2. 決定資產（股票，房地產，FX，ETF，債卷）
3. 決定產業 (科網)
4. 決定股份
5. 計算估值
6. 圖表分析

## 大趨勢 (同步指標)
1. 利率
   * (首次)上升：熊(三)轉牛(一)
   * (首次)下跌：牛(三)轉熊(一)
   * TradingView -> Indicators -> FEDFUNDS
2. 失業率
   * 連續上升3個月：牛(三)轉熊(一) 
   * 連續下跌3個月：熊(三)轉牛(一)
   * < 5% / 新低：牛三
   * Trading Economics: United States Unemployment Rate
   * TradingView: UNRATE
3. INFLATION
   * 連跌3個月：牛轉熊(2-3%)
   * 連升3個月：熊轉牛(1-2%)

## 大趨勢 (領先指標)
1. 製造業員工平均工時
   * Investing.com (United Status Average Weekly Hours)
   * 升 (牛)
   * 跌 (熊)
2. M2
3. 十年期國庫債卷及聯邦基金利差 (TradingView: US10Y)
4. US10Y - FEDFUNDS > 0 (Inverted? 牛一，熊二)
5. US10Y - FEDFUNDS < 0 (停止加息，牛三)
6. 建築許可 
   * Investing.com (US building permits)
7. US10Y - US01Y > 0 (good)
8. US10Y - US01Y < 0 (bad)

* Philly Fed United States Leading Index (L1)
* Philly Fed US Coincident Index (L2)
* US Lagging Index (L3)
* L1 growth rate < L2 & L3 Growth Rate -> (熊)
* L1 growth rate > L2 & L3 Growth Rate -> (牛)
* Search Macro Micro Leading Index (Year to Year)
* The conference Board

## 大趨勢 (如何看)
1. 熊轉牛：領先指標 + FEDFUNDS 減無可減 + FEDFUNDS 首次加息
2. 牛轉熊：FEDFUNDS 首次加息
3. 加息週期：牛 / 減息週期：熊

## 股票
## Beta Coefficient
1. < 1 : 低 (升得比指數慢)
2. = 1 : 一般 (升得和指數一樣)
3. > 1 : 高 (升得比指數快)
* 牛市：1.5-2
* 熊市：0.8-1.2

## ETF
1. 行業
   * Asset class
   * Sector
2. Size/Vol
   * Total Assets
   * Volume
3. Leverage / Inverse
   * 牛市可以 Leverage
   * Inverse 難
4. 相關性

### 選股
1. Balance Sheet (資產負債表)
   * 資產 - 負債 = 股東權益
2. Income Statement (賺錢能力)
   * 收入 - 支出 = 盈利

3. Cash Flow ()
* 選股原則_賺價_指標.png

### 指標
* ROE (Return On Equity, 股本回報率) -> 資產型
* EPSg (Earnings per Share, 每股盈利增長) -> others
* 最好是兩個指標都 Pass
* 若不是兩個指標都 Pass，Alternative 選法如下
  1. 判斷要買的公司是 資產型 / 增長型
  2. 資產型(e.g: 銀行，房地產...)，看ROE是否ok
  3. 增長型(e.g: 科技股)，看EPSg是否ok

### 選啥
* 優質股 Indicators： Net Income g vs EPSg
1. 純利(Net Income)與EPS的方向近乎一致 (一致：代表沒有做數)
2. ROE: 12%+ 成長方向
3. 維持 5-10 年期
4. 同行比較 (同 industry 的股票如何)
5. 突發事故 (COVID，Recession?) (若有，可以有1年例外)
* 選股原則_賺價.png
* 選股原則_賺價_指標.png
* 選股原則_賺價_指標結果.png

* 收息股
1.  ROE: 8%+
2.  EPSg: 5%
3.  股息率 > 3% (穩定？)
4.  配息率 (Dividend Payout Ratio) > 50% (穩定？)

### Source
* Source: MorningStar -> Key Metrics
  * Profitability and Efficiency -> Return on equity (%) (ROE)
  * Growth -> EPS (%) - Year Over Year
  * Growth -> Net Income - Year Over Year 
* 股息 Source: MorningStar -> Dividends 
  * Dividends & Splits -> Dividend per share
  * Dividends & Splits -> Payout Ratio (%)
  * Dividends & Splits -> Total Yield (%)
  * TradingView -> Indicators -> Dividend yield

### Screener
* Finviz

## 估值
1. NAVPS (Net Asset value per share) -> 重資產的公司 (市帳率, PB Ratio)
   * GuruFocus -> Book Value
2. EPS -> 盈利/增長的公司 (市盈率, PE Ratio)
3. EPS * PE = 合理價
4. ROE * PB = 合理價
5. PE 市盈率
6. PEG 市盈增長率
   * = 1: 正常
   * < 1: 低
   * > 1: 高 (貴)
7. PE = PE * Beta
8. PEG = PEG * Beta


## Pro
1. 組合管理
   * 用長遠目光看待投資
2. 交易法則
3. 部署交易系統
   * Profit and Loss Ratio (P/L Ratio)
   * 風險1，回報5 -> 勝率 17%
   * 風險1，回報3 -> 勝率 25%
   * 風險1，回報2 -> 勝率 34%
   * 風險1，回報1 -> 勝率 50%
   * 推高止賺

## 三原則
1. 升穿/跌穿 3 天
2. 3 %

## 型態分析
* 三點
* 第三點 用 candlestick 來畫
* 上昇趨勢買 / 下降趨勢賣
* TradingView -> Add ray
* TradingView -> Correlation 