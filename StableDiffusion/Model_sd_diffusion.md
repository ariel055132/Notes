# Some Useful Models
1. ouka_gufeng_s1
    * https://civitai.com/models/95718/oukagufeng?modelVersionId=102214
    * 优化器(sampler)使用UniPC
    * 放大算法推荐(Upscaler)使用 R-ESRGAN 4x+
    * VAE推荐：**novelailatest**（素雅表现），**vae-ft-mse-840000**（场景）
    * https://huggingface.co/a1079602570/animefull-final-pruned/blob/main/novelailatest-pruned.vae.pt (novelailatest)
    * https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.ckpt (vae-ft-mse-840000)

2. ouka_star
   * https://civitai.com/models/104453/oukastar
   * 优化器使用DPM++ SDE Karras，UniPC，DPM++ 2S a Karras
   * 放大算法推荐使用 R-ESRGAN 4x+
   * VAE推荐：animevae，anything-v4.0，ClearVAE，**vae-ft-mse-840000**(场景)