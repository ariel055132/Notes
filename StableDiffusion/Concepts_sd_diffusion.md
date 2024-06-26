# Notes
## Hires.fix (High Resolution Fix，高解析度修復)
1. Hires. Fix 目的是將AI生成的圖片變成高清大圖
2. 流程：AI根據輸入的Prompt跑初稿，利用放大演算法(Upscale)將圖的大小放大到指定的長寬，在將整張放大的圖以img2img的方式重新算一次，最後產生高清大圖 
3. 若需要放大真人圖片，Hires.fix 的 Upscaler 傾向使用 **R-ESRGAN 4x+**；若是二次元/動漫圖片則傾向使用 **R-ESRGAN 4x+ Anime6**
4. Hires steps: 指定Upscale後的圖，需要重跑幾次重繪步驟 (0 代表不重製)，通常20-30
5. Denoising streangth: 一張圖要加多少Noise。Range為0-1。0代表完全不加雜點(完全不重畫)；1代表完全被雜點代替(產生完全不相關的圖)；0.5通常由顯著的顔色光影改變；0.75連結構跟人物姿態都會有很明顯的變動
6. Upscale by: 放大程度

## VAE (Variable Auto Encoder)
1. 改善Checkpoint model生成出來的圖像，顔色
2. Download VAE
3. stable-diffusion-webui/models/VAE
4. settings -> Stable Diffusion -> SD VAE 選擇所需VAE

## Negative Prompts
* 避免產生出奇怪的圖片
### 基本常用 negative prompts
* worst quality, normal quality, low quality, low res, blurry, text, watermark, logo, banner, extra digits, cropped, jpeg artifacts, signature, username, error, sketch ,duplicate, ugly, monochrome, horror, geometry, mutation, disgusting
### 動漫人物用 negative prompts
* bad anatomy, bad hands, missing fingers, extra fingers, three hands, three legs, bad arms, missing legs, missing arms, poorly drawn face, bad face, fused face, cloned face, three crus, fused feet, fused thigh, extra crus, ugly fingers, horn, realistic photo, huge eyes, worst face, 2girl, long fingers, disconnected limbs
### 真實人物用 negative prompts
* bad anatomy, bad hands, missing fingers, extra fingers, three hands, three legs, bad arms, missing legs, missing arms, poorly drawn face, bad face, fused face, cloned face, three crus, fused feet, fused thigh, extra crus, ugly fingers, horn, cartoon, cg, 3d, unreal, animate, amputation, disconnected limbs
### 非成人內容 negative prompts
* nsfw, nude, censored