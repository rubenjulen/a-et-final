import time, torch, torchaudio as ta, sys
torch.set_num_threads(4)
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
t0=time.time(); m=ChatterboxMultilingualTTS.from_pretrained(device="cpu"); print('load',round(time.time()-t0,1),flush=True)
T="Welkom bij AI en Ethics. In deze module onderzoek je wat jullie eigen AI-oplossing doet met mensen, en wie daarover beslist. Denk bijvoorbeeld aan een bank in Paramaribo die een model gebruikt om leningen te beoordelen."
for name,kw in [('standaard',{}),('rustig',{'exaggeration':0.35,'cfg_weight':0.4})]:
    t0=time.time(); w=m.generate(T, language_id="nl", **kw); ta.save(f'video/samples/stemproef_chatterbox_{name}.wav', w, m.sr)
    print(name, 'sec', round(time.time()-t0,1), 'audio', round(w.shape[-1]/m.sr,1), flush=True)
