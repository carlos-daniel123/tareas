import h5py
import json

with h5py.File('keras_model.h5', 'r') as f:
    print("Top level keys:", list(f.keys()))
    for key in f.keys():
        if isinstance(f[key], h5py.Dataset):
            print(f"Dataset {key}: {f[key].shape}")
        else:
            print(f"Group {key}: {list(f[key].keys()) if hasattr(f[key], 'keys') else 'no keys'}")
    
    # Intentar model_config
    if 'model_config' in f:
        config = f['model_config'][()]
        print("model_config found")
        try:
            config_json = json.loads(config.decode('utf-8'))
            print(json.dumps(config_json, indent=2))
        except:
            print("Not JSON")
    else:
        print("No model_config")