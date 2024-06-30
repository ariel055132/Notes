# Notes
## Hires.fix
1. Hires. Fix 的全名為 High Resolution Fix（高解析度修復），其目的是將AI生成的圖片變成高清大圖
2. 流程：AI根據輸入的Prompt跑初稿，利用放大演算法(Upscale)將圖的大小放大到指定的長寬，在將整張放大的圖以img2img的方式重新算一次，最後產生高清大圖 
3. 若需要放大真人圖片，Hires.fix 的 Upscaler 傾向使用 **R-ESRGAN 4x+**；若是二次元/動漫圖片則傾向使用 **R-ESRGAN 4x+ Anime6**
4. Hires steps: 指定Upscale後的圖，需要重跑幾次重繪步驟 (0 代表不重製)，通常20-30
5. Denoising streangth: 一張圖要加多少Noise。Range為0-1。0代表完全不加雜點(完全不重畫)；1代表完全被雜點代替(產生完全不相關的圖)；0.5通常由顯著的顔色光影改變；0.75連結構跟人物姿態都會有很明顯的變動
6. Upscale by: 放大程度