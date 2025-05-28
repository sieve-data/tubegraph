---
title: Instruction tuning with synthetic data
videoId: BJ98vicRYHg
---

From: [[hu-po]] <br/> 

[[Finetuning machine learning models | Instruction tuning]] is a crucial process that transforms a pre-trained model, like GPT-4, from merely predicting the next token into a conversational assistant capable of answering questions [00:14:15]. This involves fine-tuning the model on specialized [[Data set curation and synthetic data utilization | instruction data sets]] or assistant data sets, where it learns to respond in a question-and-answer format [00:14:30].

## Generating Synthetic Data for Visual Instruction Tuning

The "secret sauce" behind the initial success of the Llava model (Large Language and Vision Assistant) was the use of [[synthetic training data for AI | machine-generated instruction following data]] [00:12:07]. This innovative approach involved using the text-only version of GPT-4 to generate language-image data, without actually feeding the image itself to GPT-4 [00:12:15].

Here's how the [[synthetic_data_generation_and_its_applications | synthetic data generation]] process worked:
1.  **Input Context**: Developers provided GPT-4 with a textual description of an image, which included captions and bounding box information (e.g., coordinates for objects like a car, people, backpack, suitcase) [00:12:42].
2.  **Question Generation**: GPT-4, without seeing the actual image, was prompted to generate a series of "fake questions" and answers based *only* on the provided text description [00:13:20].
3.  **Instruction Following Dataset Creation**: This process effectively created an instruction-following dataset for visual images without ever using the visual images to prompt GPT-4 [00:13:51]. For example, given a description of a car in a parking lot, GPT-4 might generate questions like "Where is the vehicle parked?" and answer "It's parked in an underground parking area" [00:15:05]. These answers are derived from the text-based context rather than image understanding [00:15:11].

The resulting dataset contained multi-turn conversations, though in practice, the number of turns typically did not exceed three [00:39:09]. The format of these conversations, including system messages and the order of questions and visual information, played a significant role in the model's behavior [00:40:22].

## Application in Llava Models

Llava fine-tunes its large model using this [[finetuning_with_synthetic_data | machine-generated instruction following data]] [00:12:24]. In the first stage of training (pre-training for feature alignment), Llava uses single-turn conversations where an image-text pair from a dataset like CC3M is treated as an instruction-following task to describe the image [00:46:14]. In this stage, only the projection matrix connecting the vision encoder to the language model is trained, while the vision encoder and language model remain frozen [00:46:57]. This makes the training process highly efficient and allows for local execution on GPUs [00:47:17].

In a second stage, the model continues to keep the visual encoder frozen but updates the weights of the language model, often through [[techniques_for_efficient_model_finetuning | LoRA fine-tuning]] [00:49:18].

## Benefits and Implications

*   **Efficiency**: Using pre-trained models and then only tuning a small projection layer (MLP) means that additional tuning can be completed very quickly—around one day on a single A100 node (8 GPUs) [01:00:07]. This is significantly less compute and training data compared to other methods [01:33:31].
*   **Accessibility**: This approach makes state-of-the-art LLM research more accessible, as it does not require training models from scratch [01:01:07].
*   **Performance**: Despite the relatively simple architecture and limited *additional* training data (e.g., 1.2 million publicly available data points for fine-tuning), Llava 1.5 achieves state-of-the-art results across 11 different benchmarks [01:00:15], even outperforming models with billions of trainable parameters [01:34:06]. This highlights the power of effectively utilizing pre-trained components [01:00:45].
*   **Data-Centric Research**: This work signifies a shift in machine learning research focus from complex model architectures to the strategic curation and generation of data [01:05:54]. The "training recipe" and "data mixture" become the primary hyperparameter space to explore [01:06:46].
*   **New Paradigm**: The ability to use models to generate data to train better models creates a "virtuous cycle" [01:46:42]. For example, Llava itself could be used to create datasets for specific tasks, and a future model could fine-tune on GPT-4V generated data to create a multimodal equivalent of Vuna [01:08:26].

While this method is powerful, it relies heavily on the intelligence embedded in the underlying pre-trained models (like Clip and Vuna), which were trained with significant time and resources [01:00:45]. However, the success of this simple, composite approach suggests that effectively combining powerful pre-trained components and applying [[finetuning_audio_generation_models | instruction tuning]] with high-quality [[Data set curation and synthetic data utilization | synthetic data]] can yield impressive results without prohibitive costs [01:34:25].