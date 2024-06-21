# Prompt Basic Rules
## 正向 / 反向 prompt
* 正向prompt包括masterpiece, best quality等，可以用來描述畫質和畫面。
* 反向prompt則包括nsfw（not safe for work）、lowres、bad anatomy等，可以根據畫面情況選擇不想出現的畫面。

## 符號
* "+" 和 "AND" ：這兩個符號都用於連接短關鍵字，以表示您希望同時滿足這些條件。使用 “AND” 時，需要在兩端加上空格。例如『beach + sun glasses』 或 『beach AND sun glasses』
* “|”：這是循環繪製符號（融合符號），用於在多個 Prompt 之間創建循環繪製效果。例如『(green hair：1.1) | (black hair：1.4)”』，Ai 會根據這些權重在 green hair 和 black hair 之間循環繪製，你就能得到黑綠漸層的髮色啦。

# Prompts Tested 1
* SBGF, 1 girl solo, perfect_hand, (8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.4), (extremely detailed CG unity 8k wallpaper), ,full body, (neon lights:1.2), machop, hanfu, <lora:SBGF:1>
* lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, easynegative, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), low res, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, strange fingers, bad hand, mole, ((extra legs)), ((extra hands)), badhandv4, ng_deepnegative_v1_75t

# Prompts Tested 2
1. masterpiece,(masterpiece, top quality, best quality),Chinese clothing, outdoors, upper body, looking at the viewer, 1 girl, flowers around, delicate face **(Positive Prompt)**
2. bad hands, Dark skin,((nsfw:1.3)),(EasyNegative:1.3),(badhandsv5-neg:1.5),(ng_deepnegative_v1_75t:1.2),(worst quality:1.5),(low quality:1.2),watermark,username,text,(cameltoe:1.3),((realistic:1.3)),((long pointy ears:1.3)),((forehead:1.3)),((watermark:1.3)),(((animal ears:1.3))),jacket, **(Negative Prompt)**
3. ouka_gufeng_s1 **(model)**
4. 7 **(CFG scale)**
5. UniPC **(Sampler)**
6. R-ESRGAN 4x+ **(Hires.fix-Upscaler)**
7. 25 / 20 **(Hires.fix-Hires Steps)**
8. 0.6 **(Hires.fix-Denoising strength)**
9. 2 **(Hires.fix-Upscale by)**
10. 2372327 / 23723290 **(Seed)**
11. 2 **(Batch size)**
12. 2 **(Clip skip)**

# Prompts Tested 3
1. masterpiece,(masterpiece, top quality, best quality),1girl, hair ornament, play with rabbit, dress,  solo, full body, night, moon, sky, mountain, night sky, lantern, **(Positive Prompt)**
2. Dark skin,((nsfw:1.3)),(EasyNegative:1.3),(badhandsv5-neg:1.5),(ng_deepnegative_v1_75t:1.2),(worst quality:1.5),(low quality:1.2),watermark,username,text,(cameltoe:1.3),((realistic:1.3)),((long pointy ears:1.3)),((forehead:1.3)),((watermark:1.3)),(((animal ears:1.3))),jacket, **(Negative Prompt)**
3. ouka_gufeng_s1 **(model)**
4. 7 **(CFG scale)**
5. 25 **(Steps)**
6. UniPC **(Sampler 優化器)**
7. 1816323143 **(Seed)**
8. 2 **(Clip skip)**
9. R-ESRGAN 4x+ **(Hires.fix-Upscaler 放大算法)**
10. 20 **(Hires.fix-Hires steps)**
11. 0.7 **(Hires.fix-Denoising strength)**
12. 2 **(Hires.fix-Upscale by)** 

# Prompts Tested 4


# Future Problem
1. Checkpoint主模型和Vae，Lora，embedding (Texture Inversion)、hypernetwork這些模型又有什麼區別

# Notes
## Hires.fix
1. Hires. Fix 的全名為 High Resolution Fix（高解析度修復），其目的是將AI生成的圖片變成高清大圖
2. 流程：AI根據輸入的Prompt跑初稿，利用放大演算法(Upscale)將圖的大小放大到指定的長寬，在將整張放大的圖以img2img的方式重新算一次，最後產生高清大圖 
3. 若需要放大真人圖片，Hires.fix 的 Upscaler 傾向使用 R-ESRGAN 4x+；若是二次元/動漫圖片則傾向使用 R-ESRGAN 4x+ Anime6
4. Hires steps: 指定Upscale後的圖，需要重跑幾次重繪步驟
5. 
