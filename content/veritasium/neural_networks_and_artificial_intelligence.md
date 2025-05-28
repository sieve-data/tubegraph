---
title: Neural networks and artificial intelligence
videoId: GVsUOuSjvcg
---

From: [[veritasium]] <br/> 

Artificial intelligence (AI) is a field that has seen periods of both intense research and relative inactivity, driven by advancements in computing power and algorithmic understanding <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

## Early Developments: Perceptrons and the First AI Winter

The term "artificial intelligence" was first coined in 1956 <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. A significant early development was the Perceptron, built in 1958 by Cornell University psychologist Frank Rosenblatt <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. The Perceptron was designed to mimic how neurons fire in the human brain <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

### How a Perceptron Works
A basic model of a neuron's function involves an individual neuron either firing or not, represented as a one or a zero <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. The input to one neuron comes from the output of other neurons, with varying connection strengths, or "weights" <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. These weights can be positive (excitatory) or negative (inhibitory) <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. To determine if a neuron fires, the activation of each input neuron is multiplied by its weight, and these products are summed <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. If this sum exceeds a "bias" value, the neuron fires <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>. This process is essentially a vector dot product <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

Rosenblatt's Perceptron used 400 photocells arranged in a 20x20 pixel grid as input, with each pixel's brightness acting as an input neuron's activation <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. These were connected to a single output neuron via adjustable weights <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.

### Training the Perceptron
The goal was to distinguish between images, such as rectangles and circles <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. Training involved showing the Perceptron a series of images and adjusting its weights <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>. Initially, weights were set to zero <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>. If the output was correct, no changes were made <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. If incorrect, weights were adjusted: input activations were added if the neuron should have fired but didn't, or subtracted if it fired but shouldn't have <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. This algorithm was proven to always converge if the categories were separable <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

The Perceptron could distinguish shapes and letters <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. Rosenblatt claimed it could differentiate cats from dogs and was capable of "original thought" <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>. Media coverage was highly optimistic, with the New York Times calling it "the embryo of an electronic computer" capable of advanced human-like actions and consciousness <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.

### The First AI Winter
In reality, the Perceptron's capabilities were limited; it could not, for instance, tell cats from dogs <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>. These and other limitations were detailed in a 1969 book by MIT researchers Minsky and Papert <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>. This led to a "bust period" for artificial neural networks and AI, known as the first AI winter <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>. Rosenblatt passed away during this period <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.

## AI Resurgence and Deep Neural Networks

### ALVINN and the Second AI Lull
In the 1980s, AI saw a resurgence, notably with researchers at Carnegie Mellon creating one of the first self-driving cars <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>. This vehicle was steered by an artificial neural network called ALVINN, which improved upon the Perceptron by including a hidden layer of artificial neurons between input and output <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. ALVINN received 30x32 pixel images of the road, and its layers performed matrix multiplications to determine the steering angle <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>. Training involved a human driving the vehicle, and the network's weights were adjusted using backpropagation to match the human's steering <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>. Although ALVINN learned to identify road markings, its speed was limited by the rate of matrix multiplication <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>.

Despite these advancements, artificial neural networks still struggled with tasks like distinguishing cats and dogs, leading to another AI lull in the 1990s <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.

### The Deep Learning Era and ImageNet
By the mid-2000s, researchers largely focused on improving algorithms <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>. However, researcher Fei-Fei Li proposed that the problem might be a lack of sufficient training data <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>. From 2006 to 2009, she created ImageNet, a groundbreaking database of 1.2 million human-labeled images, the largest of its kind at the time <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.

From 2010 to 2017, ImageNet hosted an annual contest where software programs competed to detect and classify images into 1,000 different categories <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. The performance was judged using the "top-5 error rate," which measures how often the correct category is *not* among the five highest neuron activations <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.

In 2010, the best performer had a top-5 error rate of 28.2% <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>. A year later, it improved to 25.8% <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>. Then, in 2012, AlexNet, an artificial neural network from the University of Toronto, achieved a remarkable 16.4% error rate <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.

:::info AlexNet's Breakthrough
AlexNet's success was attributed to its size and depth: it had eight layers and 500,000 neurons, requiring 60 million weights and biases to be adjusted during training <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>. Processing a single image involved 700 million math operations <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>. The team pioneered the use of GPUs (graphical processing units), specialized for fast parallel computations, to manage this intensive training <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.
:::

The success of AlexNet demonstrated that the scale of the neural network was key to its performance <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>. Following this breakthrough, the top-5 error rate in the ImageNet competition plummeted, reaching 3.6% in 2015, which is considered better than human performance <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>. The neural network that achieved this had 100 layers of neurons <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>. This signaled a future of ever-increasing demand for larger neural networks <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.

## The Resurgence of Analog Computing for AI

The increasing demand for larger neural networks poses several challenges for traditional digital computers:
*   **Energy Consumption:** Training a neural network can consume as much electricity as three households annually <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>.
*   **Von Neumann Bottleneck:** In modern digital computers, data is stored in memory and accessed via a bus. For the massive matrix multiplications required by deep neural networks, most time and energy are spent fetching weight values rather than on computation itself <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
*   **Limitations of Moore's Law:** The long-standing trend of doubling transistors on a chip every two years is facing fundamental physical challenges as transistor size approaches that of an atom <a class="yt-timestamp" data-t="14:10:00">[14:10:00]</a>.

This "perfect storm" of factors is setting the scene for a resurgence of [[future_potential_of_analog_computers_in_ai | analog technology]] <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a> <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>. Digital computers are reaching their limits, while neural networks are exploding in popularity, primarily relying on matrix multiplication <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a>. Crucially, neural networks do not require the extreme precision of digital computers; slight variability in components or conditions can be tolerated <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>. This makes [[analog_computing_in_machine_learning_and_ai_applications | analog computers]] well-suited for these tasks.

### Mythic AI: Analog Chips for Neural Networks
Mythic AI, an analog computing startup, is creating analog chips specifically to run neural networks <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>. They demonstrated AI algorithms like augmented/virtual reality rendering, pose capture, and depth estimation <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>.

Their approach repurposes digital flash storage cells <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. Normally, these cells store a 1 or a 0 by trapping or not trapping electrons on a floating gate, which prevents or allows current flow <a class="yt-timestamp" data-t="15:59:00">[15:59:00]</a>. Mythic's innovation is to use these cells as variable resistors by precisely controlling the number of electrons on each floating gate <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>. The greater the number of electrons, the higher the resistance <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>.

When a small voltage is applied, the resulting current (I) is equal to V/R, or voltage (V) times conductance (G), where conductance is the reciprocal of resistance (R) <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>. Thus, a single flash cell can multiply two values (voltage and conductance) <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>.

To run a neural network, Mythic's chips write all the weights to the flash cells as their conductance values <a class="yt-timestamp" data-t="17:09:00">[17:09:00]</a>. They then input activation values as voltage on the cells <a class="yt-timestamp" data-t="17:16:00">[17:16:00]</a>. The resulting current is the product of voltage times conductance (activation times weight) <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>. The cells are wired so that currents from each multiplication add together, completing the matrix multiplication <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>.

Mythic's first product can perform 25 trillion math operations per second while burning about three watts of power <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>. This contrasts with newer digital systems that perform 25-100 trillion operations per second but are large, thousand-dollar systems consuming 50-100 watts <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>. While large digital hardware is still needed for training algorithms, these analog chips are ideal for deploying AI workloads <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>. Potential applications include security cameras, autonomous systems, and inspection equipment in manufacturing <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>. Another proposed use is in smart home speakers for low-power "wake word" detection <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>.

### Hybrid Approach
Due to the inherent inexactness of analog computing, long sequences of analog operations can lead to signal distortion <a class="yt-timestamp" data-t="18:53:00">[18:53:00]</a>. To preserve the signal, a hybrid approach is used: converting from analog to digital, sending it to the next processing block, and then converting back to analog <a class="yt-timestamp" data-t="19:10:00">[19:10:00]</a>.

## Conclusion

Frank Rosenblatt initially used a digital IBM computer for his Perceptron but later built a custom [[analog_computing_in_machine_learning_and_ai_applications | analog computer]] because the digital one was too slow <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>. His idea of neural networks proved correct, and he may also have been correct about the utility of analog computing <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>.

While it's uncertain if [[future_potential_of_analog_computers_in_ai | analog computers]] will take off as digital computers did, they appear better suited for many contemporary computing tasks <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>. The human brain itself combines digital (neurons firing or not) and analog (thinking occurring everywhere simultaneously) aspects <a class="yt-timestamp" data-t="20:17:00">[20:17:00]</a>. The power of analog may be necessary to achieve true artificial intelligence, creating machines that think like humans <a class="yt-timestamp" data-t="20:28:00">[20:28:00]</a>.