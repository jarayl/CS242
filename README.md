# CS 242

Graduate level course on AI Acceleration and High Performance Computing. Taken Fall 2024 at Harvard.

# Assignment 1

Focuses on implementing and optimizing fundamental linear algebra operations in C++. Analyzed different matrix multiplication algorithms, explored low level optimization techniques for high-performance computing.

## Problems

### 1. Inner Product Matrix Multiplication
Analysis of inner product matrix-matrix multiplication (MMM) using the traditional row-wise approach, focusing on how cache efficiency and memory access patterns affect arithmetic intensity.

### 2. Outer Product Matrix Multiplication  
Analysis of outer product matrix-matrix multiplication (MMM) using the traditional column-wise approach, focusing on how cache efficiency and memory access patterns affect arithmetic intensity.

### 3. Performance Analysis and Benchmarking
Comprehensive timing analysis of both matrix multiplication implementations across different matrix sizes, measuring execution time in nanoseconds and creating visualizations to understand scalability characteristics.

### 4. CNN Exploration 
In depth exploration CNN architecture, completing forward pass by hand and performing back propogation to update weights. 

### 5. Matrix Multiplication Optimization using SIMD 
Designing SIMD based algorithm for efficient matrix multiplication, optimizing cache efficiency and data reuse. Applying SIMD to accelerate CNN forward pass. 

# Assignment 2

Covers foundational deep learning concepts, model optimization techniques, and advanced architectures. Implemented CNNs, evaluated quantization and pruning methods, explored parameter-efficient fine-tuning techniques, and built transformer components from scratch.

## Problems

### 1. CNN Training on CIFAR-10 
Implementation of a convolutional neural network using PyTorch on the CIFAR-10 image classification dataset.

### 2. Post-training Quantization on NN
Application of post-training quantization techniques on a fully-connected neural network trained on MNIST classification, reducing model size and computational requirements while analyzing the impact on accuracy and inference performance.

### 3. Convolutional Pruning
Implementation of structured filter pruning based on "Pruning Filters for Efficient ConvNets," removing redundant convolutional filters to compress neural networks while maintaining performance through systematic pruning and fine-tuning strategies.

### 4. Parameter Efficient Fine-tuning
Comparison of three fine-tuning approaches on ResNet-18: full parameter updates, frozen feature extraction, and parameter-efficient methods such as LORA, analyzing trade-offs between computational cost, memory usage, and model performance on downstream tasks.

### 5. Transformer Architecture
Implementation of core transformer components from scratch based on "Attention is All You Need," including multi-head self-attention mechanisms, positional encoding, and feed-forward networks to understand the fundamental building blocks of modern NLP architectures.

# Assignment 3 

Covers federated learning, model optimization, security, and generative diffusion models. Implemented distributed learning algorithms, explored fairness and security issues, and fine tuned multimodal generation models.

## Problems

### 1. Exploring Federated Learning (FL)
Implementation of the FedAvg algorithm to train CNN models across distributed clients using CIFAR-10 dataset, comparing federated learning performance against centralized training while analyzing communication costs and convergence behavior.

### 2. Non-IID Federated Learning and Fairness
Investigation of federated learning under realistic non-independent and identically distributed (Non-IID) data conditions, implementing fairness-aware aggregation strategies to address performance disparities across clients with heterogeneous local datasets.

### 3. Quantization of Local Models for Reduced Communication Cost
Development of model quantization techniques to compress neural network parameters, reducing communication overhead in federated learning by implementing bit-precision reduction while maintaining model accuracy and analyzing the trade-offs.

### 4. Backdoor Attacks by Malicious Clients and Defenses
Analysis of security vulnerabilities in federated learning systems by implementing backdoor attacks from malicious clients and developing defensive mechanisms such as anomaly detection and robust aggregation to maintain system integrity.

### 5. Personalized Stable Diffusion Model Implementation
Implementation of personalized text-to-image generation using Stable Diffusion v1.5, fine-tuning diffusion models on personal image datasets to create customized generative models while maintaining high-quality output and training efficiency.

### 6. Controlling Image Partitions with Text Prompts
Advanced prompt engineering and cross-modal attention mechanisms for precise control over image generation regions, implementing techniques to selectively modify specific portions of generated images based on textual instructions and spatial constraints.