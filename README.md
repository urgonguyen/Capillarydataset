# Capillary Dataset: A dataset of nail-fold capillaries captured by microscopy for diabetes detection

[**Capillary Dataset: A dataset of nail-fold capillaries captured by microscopy for diabetes detection**](https://doi.org/10.1145/3711896.3737425)    
[Hang Thi Phuong Nguyen], [Hieyong Jeong]   
KDD '25              
[Paper](https://doi.org/10.1145/3711896.3737425) | [Capillary Dataset](https://huggingface.co/datasets/HanaNguyen/Capillary-Dataset)

## 📝 TODOs

- [x] Instructions to run metric computation scripts.
- [x] Starter code snippet for L3Score.
- [x] Release responses by baselines to fully reproduce the reported numbers.
- [x] Instructions to run evaluation. 

## 🗄️ Dataset
[Capillary Dataset](https://huggingface.co/datasets/HanaNguyen/Capillary-Dataset)
The dataset are structured as follows:

```bash
Capillary dataset
    ├── Classification
        ├── data_1x1_224
        ├── data_concat_1x9_224
        ├── data_concat_2x2_224
        ├── data_concat_3x3_224
        ├── data_concat_4x1_224
        └── data_concat_4x4_224
    ├── Morphology_detection
        ├── images
        └── labels
    ├── Video
    ├── classification_original
        ├── diabetic_patients
        └── healthy_subjects
    
```
## 🧪 Evaluation

##### Setting up Conda Environment


## 📄 License

Dataset licensed under a [APACHE 2.0 License](./LICENSE).

## 🎓 Citing 

```
@article{hang2025capillary,
  title={Capillary Dataset: A dataset of nail-fold capillaries captured by microscopy for diabetes detection},
  author={Hang Thi Phuong Nguyen, Hieyong Jeong},
  journal={Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD ’25)},
  year={2025}
}
```