"""
RAGAS Evaluation Framework - Test Dataset
Pilot Record #1: Goldilocks Rule (Atomic Habits)
Source: WhiteOWL Research Workbench, captured via DevTools network layer (grey-box)
"""
from ragas import EvaluationDataset
from ragas.dataset_schema import SingleTurnSample


# ============================================================================
# Q1 - HAPPY PATH: "What is the Goldilocks Rule?"
# ============================================================================
Q1 = SingleTurnSample(
    # --- The question asked to the Workbench ---
    user_input="What is the Goldilocks Rule?",

    # --- The answer the Workbench returned (verbatim from capture) ---
    response=(
        "The Goldilocks Rule states that humans experience peak motivation when working "
        "on tasks that are right on the edge of their current abilities. This concept "
        "suggests that the greatest threat to success is not failure but boredom, as tasks "
        "that become routine can lose their interest and satisfaction over time. Therefore, "
        "maintaining motivation requires engaging in challenges that are of 'just manageable "
        "difficulty' - tasks that are neither too hard nor too easy. For example, if someone "
        "plays tennis against a much weaker opponent, they may quickly become bored, while "
        "playing against a much stronger opponent can lead to discouragement. The optimal "
        "scenario is when an individual faces a challenge that matches their skill level. "
        "Moreover, achieving a flow state often occurs when the task is about 4% beyond a "
        "person's current ability. In summary, the Goldilocks Rule emphasizes challenging "
        "oneself within a manageable difficulty range to maintain motivation and avoid "
        "boredom, which is crucial for effective habit formation and personal development."
    ),

    # --- The REAL retrieved contexts (Top 7 by cosine score, from internal_context) ---
    retrieved_contexts=[
        # score 0.8797, p178 - heading fragment (note: high score, low info)
        "Just right. THE GOLDILOCKS RULE",
        # score 0.8677, p183 - the chapter summary
        "Chapter Summary The Goldilocks Rule states that humans experience peak motivation "
        "when working on tasks that are right on the edge of their current abilities. The "
        "greatest threat to success is not failure but boredom. As habits become routine, "
        "they become less interesting and less satisfying. We get bored. Anyone can work "
        "hard when they feel motivated. It's the ability to keep going when work isn't "
        "exciting that makes the difference. Professionals stick to the schedule; amateurs "
        "let life get in the way.",
        # score 0.8279, p178 - the full definition with tennis analogy
        "While there is still much to learn, one of the most consistent findings is that the "
        "way to maintain motivation and achieve peak levels of desire is to work on tasks of "
        "'just manageable difficulty.' The human brain loves a challenge, but only if it is "
        "within an optimal zone of difficulty. If you love tennis and try to play a serious "
        "match against a four-year-old, you will quickly become bored. In contrast, if you "
        "play a professional like Roger Federer or Serena Williams, you will quickly lose "
        "motivation because the match is too difficult. The Goldilocks Rule states that "
        "humans experience peak motivation when working on tasks that are right on the edge "
        "of their current abilities. Not too hard. Not too easy.",
        # score 0.8254, p177 - chapter intro (Steve Martin)
        "19 The Goldilocks Rule: How to Stay Motivated in Life and Work. In 1955, Disneyland "
        "had just opened when a ten-year-old boy walked in and asked for a job. He set his "
        "sights on becoming a comedian and started performing in little clubs around Los "
        "Angeles. It wasn't glamorous work, but there was no doubt he was getting better.",
        # score 0.8205, p180 - core idea restated
        "The core idea of the Goldilocks Rule remains: working on challenges of just "
        "manageable difficulty - something on the perimeter of your ability - seems crucial "
        "for maintaining motivation. You need to regularly search for challenges that push "
        "you to your edge while continuing to make enough progress to stay motivated. "
        "Without variety, we get bored. And boredom is perhaps the greatest villain on the "
        "quest for self-improvement.",
        # score 0.8063, p179 - Yerkes-Dodson
        "FIGURE 15: Maximum motivation occurs when facing a challenge of just manageable "
        "difficulty. In psychology research this is known as the Yerkes-Dodson law, which "
        "describes the optimal level of arousal as the midpoint between boredom and anxiety.",
        # score 0.8055, p179 - flow state / 4%
        "And if you hit the Goldilocks Zone just right, you can achieve a flow state. A flow "
        "state is the experience of being 'in the zone' and fully immersed in an activity. "
        "They found that to achieve a state of flow, a task must be roughly 4 percent beyond "
        "your current ability.",
    ],

    # --- Your ground truth (the ideal correct answer, written from the book) ---
    reference=(
        "The Goldilocks Rule's core idea is working on challenges of just manageable "
        "difficulty - something on the perimeter of your ability - which is crucial for "
        "maintaining motivation. A task needs to be roughly 4% beyond your current ability. "
        "Successful people feel the same lack of motivation as everyone else; the difference "
        "is that they still find a way to show up despite feelings of boredom. The only way "
        "to become excellent is to be endlessly fascinated by doing the same thing over and "
        "over - one has to fall in love with boredom."
    ),
)


# ============================================================================
# Q2 - "What is the difference between best athletes and everyone?"
# ============================================================================
Q2 = SingleTurnSample(
    user_input="What is the difference between best atheletes and everyone?",

    # ANSWER THAT CAME FROM THE WORKBENCH
    response=(
        "The Goldilocks Rule suggests that the key difference between top performers and everyone "
        "else lies in their ability to maintain motivation by working on tasks that are right on the "
        "edge of their current abilities. This concept emphasizes that humans experience peak "
        "motivation when engaging with challenges that are neither too easy nor too difficult, but "
        "instead are at a level of 'just manageable difficulty'. Top performers excel not because they "
        "possess extraordinary talent or luck, but because they consistently seek out and engage with "
        "tasks that push them to their limits while still allowing for a sense of achievement. This "
        "balance is crucial for sustaining motivation, as boredom from overly simple tasks can hinder "
        "progress, while tasks that are too challenging can lead to frustration and disengagement. "
        "Additionally, successful individuals often exhibit a strong work ethic, showing up "
        "consistently even when the tasks become monotonous or less exciting. They differentiate "
        "themselves from amateurs by their dedication to practice and improvement, even when external "
        "motivation wanes. In summary, the ability of top performers to navigate the Goldilocks zone "
        "of challenge and their commitment to persistent effort, regardless of motivation, sets them "
        "apart from others."
    ),

    retrieved_contexts=[
        # 0.8608, p183 - chapter summary
        "Chapter Summary The Goldilocks Rule states that humans experience peak motivation when "
        "working on tasks that are right on the edge of their current abilities. The greatest threat "
        "to success is not failure but boredom. As habits become routine, they become less "
        "interesting and less satisfying. We get bored. Anyone can work hard when they feel motivated. "
        "It's the ability to keep going when work isn't exciting that makes the difference. "
        "Professionals stick to the schedule; amateurs let life get in the way.",
        # 0.8482, p180 - core idea + coach intro
        "The core idea of the Goldilocks Rule remains: working on challenges of just manageable "
        "difficulty - something on the perimeter of your ability - seems crucial for maintaining "
        "motivation. Improvement requires a delicate balance. You need to regularly search for "
        "challenges that push you to your edge while continuing to make enough progress to stay "
        "motivated. Without variety, we get bored. And boredom is perhaps the greatest villain on the "
        "quest for self-improvement. After my baseball career ended, I joined a weightlifting team and "
        "an elite coach visited our gym. I asked, 'What's the difference between the best athletes and "
        "everyone else? What do the really successful people do that most don't?' He mentioned the "
        "factors you might expect: genetics, luck, talent.",
        # 0.8327, p178 - tennis / just manageable difficulty
        "While there is still much to learn, one of the most consistent findings is that the way to "
        "maintain motivation is to work on tasks of 'just manageable difficulty.' The human brain "
        "loves a challenge, but only if it is within an optimal zone of difficulty. If you play tennis "
        "against a four-year-old you become bored; against Federer or Serena you lose motivation "
        "because it's too hard. Against an equal, you win a few and lose a few, your focus narrows, "
        "and you are fully invested. The Goldilocks Rule states that humans experience peak motivation "
        "when working on tasks right on the edge of their current abilities. Not too hard. Not too easy.",
        # 0.8162, p173 - explore/exploit, made for a task
        "The optimal approach depends on how much time you have. If you have a lot of time it makes "
        "sense to explore; if pressed for time, implement the best solution so far. As you explore, "
        "ask: What feels like fun to me but work to others? The mark of whether you are made for a "
        "task is not whether you love it but whether you can handle the pain of it easier than most "
        "people. When are you enjoying yourself while other people are complaining?",
        # 0.8140, p169 - competence and context
        "Competence is highly dependent on context. The people at the top of any competitive field "
        "are not only well trained, they are also well suited to the task. Genes do not determine "
        "your destiny; they determine your areas of opportunity. The areas where you are genetically "
        "predisposed to success are the areas where habits are more likely to be satisfying.",
        # 0.8133, p194 - top performers commitment
        "We've heard about Olympic gold medalists, award-winning artists, business leaders, and star "
        "comedians who have all used the science of small habits to master their craft and vault to "
        "the top of their field. Each faced different circumstances, but ultimately progressed in the "
        "same way: through a commitment to tiny, sustainable, unrelenting improvements.",
        # 0.7990, p180 - the COACH'S ANSWER (the real point)
        "Then he said something I wasn't expecting: 'At some point it comes down to who can handle the "
        "boredom of training every day, doing the same lifts over and over and over.' Really "
        "successful people feel the same lack of motivation as everyone else. The difference is that "
        "they still find a way to show up despite the feelings of boredom. Mastery requires practice, "
        "but the more you practice something, the more boring and routine it becomes.",
    ],

    # --- Your ground truth (the ideal correct answer, written from the book) ---
    reference=(
        "Successful people feel the same lack of motivation as everyone else. It all comes down to "
        "who can handle the boredom of training every day, doing the same lifts over and over. The "
        "difference is that they still find a way to show up despite the feelings of boredom."
    ),
)

# ============================================================
# Q3 | Happy Path | Professionals vs Amateurs
# ============================================================
Q3 = SingleTurnSample(
    user_input="According to Atomic Habits, what is the difference between professionals and amateurs?",
    response=(
        "According to \"Atomic Habits,\" the key difference between professionals and amateurs lies "
        "in their commitment and response to challenges. Professionals consistently stick to their "
        "schedules and commit to their goals, even when faced with difficulties or a lack of "
        "motivation. They prioritize what is important to them and work towards it purposefully, "
        "regardless of external distractions. In contrast, amateurs are more likely to let life "
        "interfere and do not maintain the same level of dedication when tasks become annoying or "
        "difficult. They may give in to the urgencies of life rather than adhering to their plans and "
        "commitments. Ultimately, professionals take action even when they don't feel like it, while "
        "amateurs often do not show up when the going gets tough."
    ),
    retrieved_contexts=[
        # 0.8724, p182 - THE exact professionals vs amateurs passage
        "There will be days when you feel like quitting. When you start a business, there will be days "
        "when you don't feel like showing up. When you're at the gym, there will be sets you don't "
        "feel like finishing. But stepping up when it's annoying or painful or draining to do so, "
        "that's what makes the difference between a professional and an amateur. Professionals stick "
        "to the schedule; amateurs let life get in the way. Professionals know what is important to "
        "them and work toward it with purpose; amateurs get pulled off course by the urgencies of "
        "life.",
        # 0.8507, p27 - Ch1 summary (atomic habits / systems) - NOTE: off-topic
        "Chapter Summary: Habits are the compound interest of self-improvement. Getting 1 percent "
        "better every day counts for a lot in the long-run. An atomic habit is a little habit that is "
        "part of a larger system. If you want better results, forget about setting goals; focus on "
        "your system instead. You do not rise to the level of your goals. You fall to the level of "
        "your systems.",
        # 0.8408, p26 - system of atomic habits - NOTE: off-topic
        "If you're having trouble changing your habits, the problem isn't you - it's your system. You "
        "do not rise to the level of your goals. You fall to the level of your systems. Atomic habits "
        "are little habits that are part of a larger system; just as atoms are the building blocks of "
        "molecules, atomic habits are the building blocks of remarkable results.",
        # 0.8393, p182 - "fall in love with boredom" - directly relevant
        "When a habit is truly important to you, you have to be willing to stick to it in any mood. "
        "Professionals take action even when the mood isn't right. They might not enjoy it, but they "
        "find a way to put the reps in. The only way to become excellent is to be endlessly "
        "fascinated by doing the same thing over and over. You have to fall in love with boredom.",
        # 0.8387, p184 - mastery requires more than habit - tangential
        "The downside of habits is that you stop paying attention to little errors. You assume you're "
        "getting better because you're gaining experience, but you may merely be reinforcing current "
        "habits, not improving them. When you want to maximize your potential and achieve elite "
        "levels of performance, you need a more nuanced approach. Habits are necessary, but not "
        "sufficient for mastery.",
        # 0.8368, p194 - top performers commitment - relevant
        "We've heard about Olympic gold medalists, award-winning artists, business leaders, and star "
        "comedians who have all used the science of small habits to master their craft and vault to "
        "the top of their field. Each faced different circumstances, but ultimately progressed in the "
        "same way: through a commitment to tiny, sustainable, unrelenting improvements.",
        # 0.8314, p183 - Goldilocks chapter summary - relevant tail
        "Chapter Summary: The Goldilocks Rule states that humans experience peak motivation when "
        "working on tasks right on the edge of their current abilities. The greatest threat to "
        "success is not failure but boredom. Anyone can work hard when they feel motivated. It's the "
        "ability to keep going when work isn't exciting that makes the difference. Professionals stick "
        "to the schedule; amateurs let life get in the way.",
    ],
    reference=(
        "Professionals stick to the schedule; amateurs let life get in the way. Professionals know "
        "what is important to them and work toward it with purpose, while amateurs get pulled off "
        "course by the urgencies of life. Anyone can work hard when motivated, but the difference is "
        "showing up even when it's boring or draining."
    ),
)

# ============================================================
# Q4 | Happy Path | Flow State
# ============================================================
Q4 = SingleTurnSample(
    user_input="What is a flow state according to Atomic Habits?",
    response=(
        "A flow state, as described in \"Atomic Habits,\" is a mental state where an individual is "
        "fully immersed in an activity, often referred to as being \"in the zone.\" This experience is "
        "characterized by intense focus, leading to a sense of happiness and peak performance, which "
        "is commonly experienced by athletes and performers during their best performances. It is "
        "noted that achieving a flow state is challenging, as it typically requires the task at hand "
        "to be approximately 4 percent beyond the individual's current ability, creating the right "
        "balance of challenge and skill to maintain engagement and satisfaction with the task "
        "involved. Additionally, the concept of flow lies between two modes of thinking as defined by "
        "psychologists: System 1, which is fast and instinctual, and System 2, which is slower and "
        "more effortful. Flow is thought to reside at the intersection of these two systems, where "
        "cognitive processes are automatic yet still require a degree of engagement."
    ),
    retrieved_contexts=[
        # 0.8779, p173 - flow definition (focus, world fades) - top scored
        "Flow is the mental state you enter when you are so focused on the task at hand that the rest "
        "of the world fades away. This blend of happiness and peak performance is what athletes and "
        "performers experience when they are \"in the zone.\" It is nearly impossible to experience a "
        "flow state and not find the task satisfying at least to some degree.",
        # 0.8569, p179 - Goldilocks Zone + 4% (the core definition)
        "And if you hit the Goldilocks Zone just right, you can achieve a flow state. A flow state is "
        "the experience of being \"in the zone\" and fully immersed in an activity. Scientists have "
        "tried to quantify this feeling. They found that to achieve a state of flow, a task must be "
        "roughly 4 percent beyond your current ability.",
        # 0.8435, p26 - system of atomic habits - NOTE: off-topic
        "A SYSTEM OF ATOMIC HABITS: If you're having trouble changing your habits, the problem isn't "
        "you - it's your system. You do not rise to the level of your goals. You fall to the level of "
        "your systems. Atomic habits are little habits that are part of a larger system; just as "
        "atoms are the building blocks of molecules, atomic habits are the building blocks of "
        "remarkable results.",
        # 0.8391, p253 - System 1 / System 2 razor's edge (author's note)
        "I have a pet theory about what happens when we achieve a flow state. Psychologists refer to "
        "the brain as operating in two modes: System 1 is fast and instinctual; System 2 controls "
        "effortful, slow thinking like calculating a difficult math problem. The more automatic a "
        "cognitive process is, the more it slides toward System 1; the more effortful, toward System "
        "2. Flow, I believe, resides on the razor's edge between System 1 and System 2.",
        # 0.8328, p226 - Csikszentmihalyi flow reference (notes section)
        "\"Flow is the mental state\": Mihaly Csikszentmihalyi, Finding Flow: The Psychology of "
        "Engagement with Everyday Life (New York: Basic Books, 2008).",
        # 0.8323, p194 - atomic habits stacking - off-topic
        "It's a bunch of atomic habits stacking up, each one a fundamental unit of the overall "
        "system. Small improvements can seem meaningless because they get washed away by the weight "
        "of the system. Gradually, as you layer small changes on top of one another, the scales of "
        "life start to move, and eventually you hit a tipping point.",
        # 0.8303, p27 - Ch1 summary - off-topic
        "Chapter Summary: Habits are the compound interest of self-improvement. Getting 1 percent "
        "better every day counts for a lot in the long-run. An atomic habit is a little habit that is "
        "part of a larger system. If you want better results, forget about setting goals; focus on "
        "your system instead. You do not rise to the level of your goals; you fall to the level of "
        "your systems.",
    ],
    reference=(
        "A flow state is the experience of being \"in the zone\" and fully immersed in an activity. "
        "Scientists found that to achieve a state of flow, a task must be roughly 4 percent beyond "
        "your current ability. In real life it's typically not feasible to quantify the difficulty of "
        "an action this way, but the core idea of the Goldilocks Rule remains: working on challenges "
        "of just manageable difficulty - something on the perimeter of your ability - seems crucial "
        "for maintaining motivation."
    ),
)

# ============================================================
# Q5 | Multi-part | Motivation factors: difficulty, boredom, flow
# ============================================================
Q5 = SingleTurnSample(
    user_input="What are the key factors that influence motivation according to the Goldilocks Rule, and how do they relate to boredom and flow?",
    response=(
        "The Goldilocks Rule states that humans experience peak motivation when working on tasks that "
        "are at the edge of their current abilities, meaning tasks that are neither too hard nor too "
        "easy. This principle highlights that individuals are most motivated when they face challenges "
        "that are just manageable in difficulty. If tasks are too easy, boredom sets in, and if they "
        "are too difficult, frustration leads to a loss of motivation. Thus, maintaining a delicate "
        "balance is crucial for sustained motivation and improvement, as tasks must remain novel and "
        "engaging to prevent boredom from derailing progress. Boredom is identified as one of the "
        "greatest threats to success. As habits become routine and predictable, they lose their "
        "excitement, leading individuals to seek novelty, which can disrupt their progress. This "
        "cycle of seeking new challenges often emerges when motivation dips, even if the original "
        "strategy was effective. Achieving a flow state, which is characterized by deep immersion and "
        "focus on an activity, occurs when the task is just slightly more challenging than one's "
        "current abilities - typically around 4% beyond their current skill level. In this state, "
        "distractions fade away, and individuals feel fully engaged and satisfied with the task at "
        "hand. In summary, the Goldilocks Rule underscores the importance of balancing challenge and "
        "skill to avoid boredom and foster motivation. By engaging in tasks that are appropriately "
        "difficult, individuals can maintain motivation, avoid boredom, and potentially enter a flow "
        "state, enhancing both performance and satisfaction in their activities."
    ),
    retrieved_contexts=[
        # 0.8832, p183 - chapter summary (peak motivation + boredom threat)
        "Chapter Summary: The Goldilocks Rule states that humans experience peak motivation when "
        "working on tasks right on the edge of their current abilities. The greatest threat to "
        "success is not failure but boredom. As habits become routine, they become less interesting "
        "and less satisfying. We get bored. Anyone can work hard when they feel motivated. It's the "
        "ability to keep going when work isn't exciting that makes the difference. Professionals "
        "stick to the schedule; amateurs let life get in the way.",
        # 0.8655, p180 - just-manageable-difficulty + boredom as greatest villain
        "The core idea of the Goldilocks Rule remains: working on challenges of just manageable "
        "difficulty - something on the perimeter of your ability - seems crucial for maintaining "
        "motivation. Improvement requires a delicate balance. You need to regularly search for "
        "challenges that push you to your edge while continuing to make progress. Behaviors need to "
        "remain novel to stay attractive and satisfying. Without variety, we get bored. And boredom "
        "is perhaps the greatest villain on the quest for self-improvement.",
        # 0.8597, p178 - tennis / just manageable difficulty / not too hard not too easy
        "One of the most consistent findings is that the way to maintain motivation is to work on "
        "tasks of 'just manageable difficulty.' The brain loves a challenge, but only within an "
        "optimal zone. Play tennis against a four-year-old and you're bored; against Federer or "
        "Serena and you lose motivation - too hard. Against an equal, your focus narrows and you're "
        "fully invested. The Goldilocks Rule states humans experience peak motivation working on "
        "tasks right on the edge of their abilities. Not too hard. Not too easy.",
        # 0.8488, p179 - Yerkes-Dodson / midpoint between boredom and anxiety
        "FIGURE 15: Maximum motivation occurs when facing a challenge of just manageable difficulty. "
        "In psychology research this is known as the Yerkes-Dodson law, which describes the optimal "
        "level of arousal as the midpoint between boredom and anxiety. Each year Martin expanded his "
        "comedy routine by a minute or two - just enough victories to stay motivated and just enough "
        "mistakes to keep working hard.",
        # 0.8303, p179 - flow state / 4% beyond ability
        "And if you hit the Goldilocks Zone just right, you can achieve a flow state. A flow state is "
        "the experience of being 'in the zone' and fully immersed in an activity. Scientists found "
        "that to achieve a state of flow, a task must be roughly 4 percent beyond your current "
        "ability.",
        # 0.8289, p180 - coach: handle the boredom / show up anyway
        "Then the coach said: 'At some point it comes down to who can handle the boredom of training "
        "every day, doing the same lifts over and over.' Really successful people feel the same lack "
        "of motivation as everyone else. The difference is that they still find a way to show up "
        "despite the feelings of boredom. Mastery requires practice, but the more you practice, the "
        "more boring and routine it becomes.",
        # 0.8280, p181 - boredom = greatest threat, novelty-seeking cycle
        "The greatest threat to success is not failure but boredom. We get bored with habits because "
        "they stop delighting us. As our habits become ordinary, we start derailing our progress to "
        "seek novelty. As soon as we experience the slightest dip in motivation, we begin seeking a "
        "new strategy - even if the old one was still working. As Machiavelli noted, men desire "
        "novelty to such an extent that those doing well wish for change as much as those doing badly.",
    ],
    reference=(
        "According to the Goldilocks Rule, peak motivation comes from working on challenges of just "
        "manageable difficulty - tasks on the edge of your current ability. To achieve a flow state, "
        "the task should be roughly 4% beyond your current ability. However, the key factor is "
        "sustaining motivation against boredom: human nature craves novelty, so doing the same thing "
        "repeatedly will eventually become boring. The greatest threat to success is not failure but "
        "boredom - and at some point it comes down to who can handle the boredom of training every "
        "day, doing the same thing over and over."
    ),
)

# ============================================================
# Q6 | Multi-part | Goldilocks + boredom problem + professionals overcome
# ============================================================
Q6 = SingleTurnSample(
    user_input="According to Atomic Habits, what is the Goldilocks Rule, why is boredom a problem, and how do professionals overcome it?",
    response=(
        "The Goldilocks Rule, as described in \"Atomic Habits,\" states that humans experience peak "
        "motivation when working on tasks that are right on the edge of their current abilities. This "
        "means that individuals are most engaged and driven when faced with challenges that are not "
        "too easy, which leads to boredom, and not too hard, which can lead to frustration and "
        "anxiety. The ideal scenario is to find tasks that provide just the right level of difficulty "
        "to maintain interest and motivation, a concept supported by the Yerkes-Dodson law, which "
        "describes the optimal level of arousal in relation to performance and task difficulty. "
        "Boredom is seen as a significant problem in the pursuit of self-improvement. As habits become "
        "routine, they often lose their novelty and excitement, leading to a decline in motivation. "
        "People may frequently switch from one habit to another in search of novelty, which can derail "
        "progress. Professionals overcome boredom by adhering to their schedules and maintaining "
        "discipline, even when the tasks at hand are not exciting. They recognize that consistency and "
        "the ability to persist through periods of boredom are what differentiate them from amateurs, "
        "who may allow distractions and lack of motivation to derail their efforts. This commitment to "
        "routine and the pursuit of small, manageable challenges helps professionals stay focused and "
        "engaged. In summary, the Goldilocks Rule emphasizes finding a balance in challenge levels for "
        "sustained motivation, while boredom remains a key threat to progress. Professionals combat "
        "this by sticking to their routines and embracing the mundane aspects of their pursuits as "
        "part of the journey towards mastery."
    ),
    retrieved_contexts=[
        # 0.8962, p183 - chapter summary (all 3 pieces in one chunk)
        "Chapter Summary: The Goldilocks Rule states that humans experience peak motivation when "
        "working on tasks right on the edge of their current abilities. The greatest threat to "
        "success is not failure but boredom. As habits become routine, they become less interesting "
        "and less satisfying. We get bored. Anyone can work hard when they feel motivated. It's the "
        "ability to keep going when work isn't exciting that makes the difference. Professionals stick "
        "to the schedule; amateurs let life get in the way.",
        # 0.8694, p180 - just-manageable-difficulty + boredom greatest villain + coach intro
        "The core idea of the Goldilocks Rule remains: working on challenges of just manageable "
        "difficulty - something on the perimeter of your ability - seems crucial for maintaining "
        "motivation. Improvement requires a delicate balance. Behaviors need to remain novel to stay "
        "attractive and satisfying. Without variety, we get bored. And boredom is perhaps the greatest "
        "villain on the quest for self-improvement.",
        # 0.8469, p178 - tennis / just manageable difficulty (the definition)
        "One of the most consistent findings is that the way to maintain motivation is to work on "
        "tasks of 'just manageable difficulty.' The brain loves a challenge, but only within an "
        "optimal zone. Tennis against a four-year-old is too easy; against Federer or Serena, too "
        "hard. Against an equal, your focus narrows and you're fully invested. The Goldilocks Rule "
        "states humans experience peak motivation working on tasks right on the edge of their "
        "abilities. Not too hard. Not too easy.",
        # 0.8440, p179 - Yerkes-Dodson + Martin example
        "FIGURE 15: Maximum motivation occurs when facing a challenge of just manageable difficulty. "
        "In psychology research this is known as the Yerkes-Dodson law, which describes the optimal "
        "level of arousal as the midpoint between boredom and anxiety. Each year Martin expanded his "
        "comedy routine by a minute or two - just enough victories to stay motivated and just enough "
        "mistakes to keep working hard.",
        # 0.8404, p181 - boredom = greatest threat + novelty-seeking cycle
        "The greatest threat to success is not failure but boredom. We get bored with habits because "
        "they stop delighting us. As our habits become ordinary, we start derailing our progress to "
        "seek novelty - jumping from one workout to the next, one diet to the next. As soon as we "
        "experience the slightest dip in motivation, we begin seeking a new strategy, even if the old "
        "one was still working.",
        # 0.8395, p182 - professionals overcome: show up, fall in love with boredom
        "When a habit is truly important to you, you have to be willing to stick to it in any mood. "
        "Professionals take action even when the mood isn't right. They might not enjoy it, but they "
        "find a way to put the reps in. The only way to become excellent is to be endlessly "
        "fascinated by doing the same thing over and over. You have to fall in love with boredom.",
        # 0.8331, p180 - coach: who can handle the boredom / show up anyway
        "The coach said: 'At some point it comes down to who can handle the boredom of training every "
        "day, doing the same lifts over and over.' Really successful people feel the same lack of "
        "motivation as everyone else. The difference is that they still find a way to show up despite "
        "the feelings of boredom. Mastery requires practice, but the more you practice, the more "
        "boring and routine it becomes.",
    ],
    reference=(
        "The Goldilocks Rule states that humans experience peak motivation when working on challenges "
        "of just manageable difficulty - tasks on the edge of their current ability, neither too hard "
        "nor too easy. Boredom is a problem because human nature craves novelty: as habits become "
        "routine they become less satisfying, and the greatest threat to success is not failure but "
        "boredom. Professionals overcome it by showing up anyway - they feel the same lack of "
        "motivation as everyone else, but they still put in the reps despite the boredom. "
        "Professionals stick to the schedule; amateurs let life get in the way."
    ),
)

# ============================================================
# Q7 | Inference | Why boredom > failure as obstacle
# ============================================================
Q7 = SingleTurnSample(
    user_input="Why does the Goldilocks Rule suggest that boredom, rather than failure, is the greatest obstacle to long-term success?",
    response=(
        "The Goldilocks Rule suggests that boredom, rather than failure, is the greatest obstacle to "
        "long-term success because individuals experience peak motivation when engaging in tasks that "
        "are right on the edge of their current abilities. When tasks become too routine or "
        "predictable, they lose their appeal and can lead to boredom. This boredom can derail progress "
        "as individuals may seek novelty and change, often abandoning effective routines in search of "
        "new, more exciting challenges, even if the original task was still working well for them. This "
        "tendency to chase novelty in response to boredom is a major barrier to sustained effort and "
        "improvement in any area of life, including habits and skills development. The Goldilocks Rule "
        "emphasizes the importance of working on challenges that are just manageable in difficulty. "
        "When tasks are too easy, they become boring, and when they are too hard, they can lead to "
        "discouragement. The ideal zone is where one feels challenged but still capable, which keeps "
        "motivation high and promotes continuous improvement. A lack of variety in tasks can lead to a "
        "decline in motivation, making boredom a significant villain in the quest for self-improvement. "
        "Hence, maintaining interest and engagement through manageable challenges is crucial for "
        "long-term success and mastery in any field."
    ),
    retrieved_contexts=[
        # 0.8978, p183 - chapter summary (boredom = greatest threat)
        "Chapter Summary: The Goldilocks Rule states that humans experience peak motivation when "
        "working on tasks right on the edge of their current abilities. The greatest threat to success "
        "is not failure but boredom. As habits become routine, they become less interesting and less "
        "satisfying. We get bored. Anyone can work hard when they feel motivated. It's the ability to "
        "keep going when work isn't exciting that makes the difference.",
        # 0.8677, p180 - just-manageable-difficulty + boredom greatest villain
        "The core idea of the Goldilocks Rule remains: working on challenges of just manageable "
        "difficulty - something on the perimeter of your ability - seems crucial for maintaining "
        "motivation. Behaviors need to remain novel to stay attractive and satisfying. Without "
        "variety, we get bored. And boredom is perhaps the greatest villain on the quest for "
        "self-improvement.",
        # 0.8629, p181 - boredom derails progress, novelty-chasing cycle
        "The greatest threat to success is not failure but boredom. We get bored with habits because "
        "they stop delighting us. The outcome becomes expected. As our habits become ordinary, we "
        "start derailing our progress to seek novelty - jumping from one workout to the next, one diet "
        "to the next. As soon as we experience the slightest dip in motivation, we begin seeking a new "
        "strategy, even if the old one was still working. As Machiavelli noted, men desire novelty to "
        "such an extent that those doing well wish for change as much as those doing badly.",
        # 0.8538, p178 - just manageable difficulty / tennis
        "One of the most consistent findings is that the way to maintain motivation is to work on "
        "tasks of 'just manageable difficulty.' The brain loves a challenge, but only within an "
        "optimal zone. Too easy and you're bored; too hard and you lose motivation. The Goldilocks "
        "Rule states humans experience peak motivation working on tasks right on the edge of their "
        "abilities. Not too hard. Not too easy.",
        # 0.8438, p179 - Yerkes-Dodson (midpoint boredom/anxiety)
        "FIGURE 15: Maximum motivation occurs when facing a challenge of just manageable difficulty. "
        "In psychology research this is known as the Yerkes-Dodson law, which describes the optimal "
        "level of arousal as the midpoint between boredom and anxiety.",
        # 0.8380, p180 - coach: handle the boredom / show up anyway
        "The coach said: 'At some point it comes down to who can handle the boredom of training every "
        "day, doing the same lifts over and over.' Really successful people feel the same lack of "
        "motivation as everyone else. The difference is that they still find a way to show up despite "
        "the feelings of boredom. Mastery requires practice, but the more you practice, the more "
        "boring and routine it becomes.",
        # 0.8232, p181 - variable reward / boredom reduction
        "Variable rewards are a powerful way to amplify cravings because they reduce boredom. The "
        "sweet spot of desire occurs at a 50/50 split between success and failure. You need just "
        "enough winning to experience satisfaction and just enough wanting to experience desire. This "
        "is one of the benefits of following the Goldilocks Rule: working on challenges of just "
        "manageable difficulty is a good way to keep things interesting.",
    ],
    reference=(
        "The human mind craves novelty. At a certain point the same habits stop delighting us "
        "because we already know their expected outcome. When we experience even the slightest dip "
        "in motivation, we begin seeking a new strategy - even when the old one was still working. "
        "This is why boredom, not failure, is the greatest obstacle: it makes us abandon what was "
        "working. Everyone faces this on the journey of self-improvement; the answer is to fall in "
        "love with boredom. This is the core difference between a professional and an amateur - "
        "professionals stick to the schedule while amateurs let life get in the way. The only "
        "difference is showing up."
    ),
)

# ============================================================
# Q8 | Inference | Flow state <-> just manageable difficulty
# NOTE: captured on production instance (doc 1260), unlike Q1-Q7 (staging, doc 3271)
# ============================================================
Q8 = SingleTurnSample(
    user_input="How does the concept of a flow state connect to the Goldilocks Rule's idea of just manageable difficulty?",
    response=(
        "The concept of a flow state is closely connected to the Goldilocks Rule, which emphasizes the "
        "importance of engaging in tasks of just manageable difficulty. The Goldilocks Rule posits that "
        "individuals experience peak motivation when working on challenges that are right on the edge "
        "of their current abilities - not too hard, and not too easy. This optimal level of difficulty "
        "fosters engagement and motivation, as individuals are likely to lose interest in tasks that "
        "are either too simple or too challenging. For instance, playing tennis against an opponent of "
        "equal skill can lead to a state where distractions fade away, and the player becomes fully "
        "invested in the game, exemplifying the Goldilocks Rule in action. Achieving a flow state "
        "requires that a task be approximately 4 percent beyond one's current ability. This delicate "
        "balance allows individuals to push their capabilities while still feeling competent and "
        "engaged. When tasks are appropriately challenging, they can lead to the immersive experience "
        "of flow, where individuals feel \"in the zone\" and focused intently on the activity at hand. "
        "In summary, the connection between flow states and the Goldilocks Rule lies in the optimal "
        "challenge level that fosters motivation and deep engagement in tasks."
    ),
    retrieved_contexts=[
        # 0.8869, p178 - just manageable difficulty / tennis / Goldilocks definition
        "One of the most consistent findings is that the way to maintain motivation is to work on "
        "tasks of 'just manageable difficulty.' The brain loves a challenge, but only within an "
        "optimal zone. Tennis against a four-year-old is too easy; against Federer or Serena, too "
        "hard. Against an equal, your focus narrows, distractions fade away, and you are fully "
        "invested. The Goldilocks Rule states humans experience peak motivation working on tasks right "
        "on the edge of their abilities. Not too hard. Not too easy.",
        # 0.8858, p179 - Goldilocks Zone -> flow state, 4%
        "And if you hit the Goldilocks Zone just right, you can achieve a flow state. A flow state is "
        "the experience of being 'in the zone' and fully immersed in an activity. Scientists found "
        "that to achieve a state of flow, a task must be roughly 4 percent beyond your current "
        "ability.",
        # 0.8647, p183 - chapter summary
        "Chapter Summary: The Goldilocks Rule states that humans experience peak motivation when "
        "working on tasks right on the edge of their current abilities. The greatest threat to success "
        "is not failure but boredom. Anyone can work hard when they feel motivated. It's the ability "
        "to keep going when work isn't exciting that makes the difference.",
        # 0.8606, p180 - core idea, perimeter of ability
        "The core idea of the Goldilocks Rule remains: working on challenges of just manageable "
        "difficulty - something on the perimeter of your ability - seems crucial for maintaining "
        "motivation. You need to regularly search for challenges that push you to your edge while "
        "continuing to make enough progress to stay motivated. Without variety, we get bored.",
        # 0.8581, p173 - flow definition (world fades away)
        "Flow is the mental state you enter when you are so focused on the task at hand that the rest "
        "of the world fades away. This blend of happiness and peak performance is what athletes and "
        "performers experience when they are 'in the zone.' It is nearly impossible to experience a "
        "flow state and not find the task satisfying at least to some degree.",
        # 0.8522, p179 - Yerkes-Dodson
        "FIGURE 15: Maximum motivation occurs when facing a challenge of just manageable difficulty. "
        "In psychology research this is known as the Yerkes-Dodson law, which describes the optimal "
        "level of arousal as the midpoint between boredom and anxiety.",
        # 0.8304, p226 - Csikszentmihalyi flow reference (notes)
        "'Flow is the mental state': Mihaly Csikszentmihalyi, Finding Flow: The Psychology of "
        "Engagement with Everyday Life (New York: Basic Books, 2008).",
    ],
    reference=(
        "The way to maintain motivation and achieve peak levels of desire is to work on tasks of "
        "'just manageable difficulty.' The human brain loves a challenge, but only when it is within "
        "an optimal zone of difficulty. The Goldilocks Rule states that humans experience peak "
        "motivation when working on tasks right on the edge of their current abilities - not too "
        "hard, not too easy, just right. It connects to how we form habits: we need to keep the "
        "behavior as easy as possible so we can stick with it even when conditions aren't perfect, "
        "and then the little improvements and new challenges keep us engaged. Eventually, if we hit "
        "the Goldilocks Zone just right, we reach the flow state."
    ),
)

# ============================================================
# Q9 | Specific Fact | Flow state = 4% beyond current ability
# ============================================================
Q9 = SingleTurnSample(
    user_input="According to Atomic Habits, how far beyond your current ability must a task be to achieve a flow state?",
    response=(
        "To achieve a flow state, a task must be approximately 4 percent beyond your current ability. "
        "This optimal challenge helps to engage you fully in the activity, allowing you to experience "
        "heightened focus and enjoyment, which are characteristic of being \"in the zone\" or in a flow "
        "state."
    ),
    retrieved_contexts=[
        # 0.8754, p179 - THE answer chunk (4%)
        "And if you hit the Goldilocks Zone just right, you can achieve a flow state. A flow state is "
        "the experience of being 'in the zone' and fully immersed in an activity. Scientists have "
        "tried to quantify this feeling. They found that to achieve a state of flow, a task must be "
        "roughly 4 percent beyond your current ability.",
        # 0.8540, p173 - flow definition
        "Flow is the mental state you enter when you are so focused on the task at hand that the rest "
        "of the world fades away. This blend of happiness and peak performance is what athletes and "
        "performers experience when they are 'in the zone.' It is nearly impossible to experience a "
        "flow state and not find the task satisfying at least to some degree.",
        # 0.8339, p131 - showing up / two-minute ritual - OFF-TOPIC
        "The point is not to do one thing. The point is to master the habit of showing up. A habit "
        "must be established before it can be improved. You have to standardize before you can "
        "optimize. The more you ritualize the beginning of a process, the more likely it becomes that "
        "you can slip into the state of deep focus that is required to do great things.",
        # 0.8317, p183 - Goldilocks chapter summary
        "Chapter Summary: The Goldilocks Rule states that humans experience peak motivation when "
        "working on tasks right on the edge of their current abilities. The greatest threat to "
        "success is not failure but boredom. Anyone can work hard when they feel motivated. It's the "
        "ability to keep going when work isn't exciting that makes the difference.",
        # 0.8312, p134 - Two-Minute Rule summary - OFF-TOPIC
        "Chapter Summary: Habits can be completed in a few seconds but continue to impact your "
        "behavior for minutes or hours afterward. The Two-Minute Rule states, 'When you start a new "
        "habit, it should take less than two minutes to do.' Standardize before you optimize.",
        # 0.8292, p130 - gateway habit - OFF-TOPIC
        "A new habit should not feel like a challenge. The actions that follow can be challenging, but "
        "the first two minutes should be easy. What you want is a 'gateway habit' that naturally "
        "leads you down a more productive path. Your goal might be to run a marathon, but your "
        "gateway habit is to put on your running shoes.",
        # 0.8274, p42 - mental space / freedom - OFF-TOPIC
        "It's only by making the fundamentals of life easier that you can create the mental space "
        "needed for free thinking and creativity. When you have your habits dialed in, your mind is "
        "free to focus on new challenges and master the next set of problems.",
    ],
    reference=(
        "In order to achieve a flow state, a task must be roughly 4 percent beyond your current "
        "ability."
    ),
)

# ============================================================
# Q10 | Specific Fact | Yerkes-Dodson law
# BUG: internal_sources & external_sources both empty despite valid citation in answer
# ============================================================
Q10 = SingleTurnSample(
    user_input="What is the Yerkes-Dodson law according to Atomic Habits?",
    response=(
        "The Yerkes-Dodson law, as discussed in \"Atomic Habits,\" describes the relationship between "
        "arousal and performance. It posits that maximum motivation occurs when facing challenges that "
        "are of just manageable difficulty. This law suggests that there is an optimal level of arousal "
        "that lies between boredom and anxiety. When individuals are engaged in tasks that are neither "
        "too easy nor too difficult, they are likely to perform at their best. This concept aligns with "
        "the Goldilocks Rule, which states that humans experience peak motivation when working on tasks "
        "that are right at the edge of their current abilities, avoiding both boredom and overwhelming "
        "challenges. For example, a comedian's career illustrates this principle, as they may expand "
        "their routine gradually - adding just enough new material to maintain interest and motivation "
        "while ensuring some guaranteed successes to keep them engaged and striving for improvement."
    ),
    retrieved_contexts=[
        # 0.8669, p179 - THE answer chunk (Yerkes-Dodson)
        "FIGURE 15: Maximum motivation occurs when facing a challenge of just manageable difficulty. "
        "In psychology research this is known as the Yerkes-Dodson law, which describes the optimal "
        "level of arousal as the midpoint between boredom and anxiety. Martin's comedy career is an "
        "excellent example of the Goldilocks Rule in practice. Each year, he expanded his comedy "
        "routine - but only by a minute or two. There were just enough victories to keep him "
        "motivated and just enough mistakes to keep him working hard.",
        # 0.8470, p93 - 2nd Law summary - OFF-TOPIC
        "Chapter Summary: The 2nd Law of Behavior Change is make it attractive. Habits are a "
        "dopamine-driven feedback loop. When dopamine rises, so does our motivation to act. It is the "
        "anticipation of a reward - not the fulfillment of it - that gets us to take action.",
        # 0.8438, p82 - Four Laws cheat sheet - OFF-TOPIC
        "Make the cues of good habits obvious and visible. The 2nd Law: Make It Attractive. The 3rd "
        "Law: Make It Easy. The 4th Law: Make It Satisfying. HOW TO BREAK A BAD HABIT: Inversion of "
        "the 1st Law: Make It Invisible. Reduce exposure - remove the cues of your bad habits from "
        "your environment.",
        # 0.8394, p48 - Four Laws questions - OFF-TOPIC
        "Whenever you want to change your behavior, you can simply ask yourself: 1. How can I make it "
        "obvious? 2. How can I make it attractive? 3. How can I make it easy? 4. How can I make it "
        "satisfying? The answers to those questions can be found somewhere in these four laws.",
        # 0.8387, p165 - Four Laws tactics - OFF-TOPIC
        "The 2nd Law: Make It Attractive. Use temptation bundling. Join a culture where your desired "
        "behavior is the normal behavior. The 3rd Law: Make It Easy. Reduce friction. Prime the "
        "environment. Use the Two-Minute Rule. The 4th Law: Make It Satisfying. Use reinforcement.",
        # 0.8349, p26 - system of atomic habits - OFF-TOPIC
        "A SYSTEM OF ATOMIC HABITS: If you're having trouble changing your habits, the problem isn't "
        "you - it's your system. You do not rise to the level of your goals. You fall to the level of "
        "your systems.",
        # 0.8345, p27 - Ch1 summary - OFF-TOPIC
        "Chapter Summary: Habits are the compound interest of self-improvement. Getting 1 percent "
        "better every day counts for a lot in the long-run. If you want better results, forget about "
        "setting goals; focus on your system instead.",
    ],
    reference=(
        "Maximum motivation occurs when facing a challenge of just manageable difficulty. In "
        "psychology research this is known as the Yerkes-Dodson law, which describes the optimal "
        "level of arousal as the midpoint between boredom and anxiety."
    ),
)

# ============================================================
# Q13 | Out-of-Scope | Cryptocurrency (not in book)
# RESULT: PASS - system correctly declined, no hallucination
# ============================================================
Q13 = SingleTurnSample(
    user_input="Does Atomic Habits discuss cryptocurrency investing?",
    response=(
        "\"Atomic Habits\" does not specifically discuss cryptocurrency investing. The book focuses on "
        "the principles of habit formation and personal improvement, emphasizing how small changes can "
        "lead to significant results over time. It teaches strategies for building better habits and "
        "breaking bad ones without delving into specific investment strategies or financial topics "
        "like cryptocurrency. The discussions are largely centered on behavioral change and "
        "productivity, rather than investment advice or market analysis."
    ),
    retrieved_contexts=[
        # 0.8100, p27 - Ch1 summary
        "Chapter Summary: Habits are the compound interest of self-improvement. Getting 1 percent "
        "better every day counts for a lot in the long-run. An atomic habit is a little habit that is "
        "part of a larger system. If you want better results, forget about setting goals; focus on "
        "your system instead. You do not rise to the level of your goals. You fall to the level of "
        "your systems.",
        # 0.8093, p26 - system of atomic habits
        "A SYSTEM OF ATOMIC HABITS: If you're having trouble changing your habits, the problem isn't "
        "you - it's your system. Atomic habits are little habits that are part of a larger system; "
        "just as atoms are the building blocks of molecules, atomic habits are the building blocks of "
        "remarkable results.",
        # 0.8027, p4 - book intro / what the book teaches
        "This book is about how to build better habits - not for a few days or weeks, but for a "
        "lifetime. Habits are the compound interest of self-improvement. The same way that money "
        "multiplies through compound interest, the effects of your habits multiply as you repeat them.",
        # 0.7985, p13 - 1 percent better
        "Success is the product of daily habits - not once-in-a-lifetime transformations. Getting 1 "
        "percent better every day for one year makes you thirty-seven times better by the time you're "
        "done. Small habits don't add up, they compound.",
        # 0.7954, p194 - commitment to improvement
        "Each faced different circumstances, but ultimately progressed in the same way: through a "
        "commitment to tiny, sustainable, unrelenting improvements. Small improvements can seem "
        "meaningless at first, but eventually you hit a tipping point.",
        # 0.7931, p18 - goals vs systems
        "Goals are about the results you want to achieve. Systems are about the processes that lead to "
        "those results. If you want better results, forget about setting goals. Focus on your system "
        "instead.",
        # 0.7902, p9 - habits and identity
        "Behavior change is really identity change. You might start a habit because of motivation, but "
        "the only reason you'll stick with one is that it becomes part of your identity.",
    ],
    reference=(
        "This information is not present in the document. Atomic Habits does not discuss "
        "cryptocurrency or investment topics. The book is about habit formation, behavior change, and "
        "personal improvement."
    ),
)















def load_dataset():
    """Returns the EvaluationDataset for RAGAS."""
    return EvaluationDataset(samples=[Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q13])
