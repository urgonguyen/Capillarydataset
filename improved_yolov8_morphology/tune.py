from ultralytics import YOLO
import itertools

param_grid = {
    'mosaic': [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    'mixup': [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
}

# Generate combinations
param_combinations = list(itertools.product(*param_grid.values()))

best_map = 0
best_params = {}
results_dict = {}
for combination in param_combinations:
    params = dict(zip(param_grid.keys(), combination))
    model = YOLO('runs/detect/train15_p2_ECA/weights/best.pt')
    results=model.train(data='data.yaml', epochs=50, **params)
    print("result {} of param: {}".format(results,params))
    #if results['metrics/mAP50(B)'] > best_map:
    #    best_map = results_dict
    #    best_params = params

#print("Best mAP: {} with Parameters: {}".format(best_map, best_params))

