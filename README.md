# metaheu_final_prj
This is my final project for metaheuristic course. A detail report in IEEE format is at report.docx
The idea of this work is originated from the paper [Evolving Multimodal Behavior With Modular Neural
Networks in Ms. Pac-Man
](https://pdfs.semanticscholar.org/3736/f7c2c310e0426df3d5cc56e0b0a78ddf1f6c.pdf) The features in the paper end up to be linear combination. From my opinion, the combination function should have some other forms. 

I try to use GA to delvelop my own agent.  In my agent design, I use an evaluation function to evaluate every successor states, and take the one with the highest evaluation score. Fix features including distance to opponent agent, distance to food, distance to the middle line, etc. Each feature comes with a weight, which will be trained in GA. The setup of GA is stated in the section 3 of the report.


