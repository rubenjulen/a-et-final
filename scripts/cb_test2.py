import time, torch, torchaudio as ta
torch.set_num_threads(4); torch.manual_seed(7)
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
m=ChatterboxMultilingualTTS.from_pretrained(device="cpu")
zinnen=["Welkom bij AI en Ethics.","In deze module onderzoek je wat jullie eigen AI-oplossing doet met mensen, en wie daarover beslist.","Denk bijvoorbeeld aan een bank in Paramaribo, die een model gebruikt om leningen te beoordelen."]
stukken=[]
for z in zinnen:
    t0=time.time(); w=m.generate(z, language_id="nl", exaggeration=0.25, cfg_weight=0.3, temperature=0.6)
    stukken += [w, torch.zeros(1,int(0.45*m.sr))]; print(round(time.time()-t0,1),flush=True)
ta.save('video/samples/stemproef_chatterbox_kalm.wav', torch.cat(stukken,dim=1), m.sr)
