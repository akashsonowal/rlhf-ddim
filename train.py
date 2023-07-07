

aesthetic_model = MLP(768)
aesthetic_model.load_state_dict(weights)

def reward_fn(imgs, device):
    clip_model.to(device)
    aesthetic_model.to(device)

    rewards = aesthetic_scoring(imgs, preprocess, clip_model, aesthetic_model_normalize, aesthetic_model)

    clip_model.to("cpu")
    aesthetic_model.to("cpu")
    
    return rewards