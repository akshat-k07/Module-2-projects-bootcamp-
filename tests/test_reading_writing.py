from lib.reading_writing import *

def test_reading_time_over_one_min():
    time = 2.54
    result = reading_time("Certainly! I will craft a single, extensive paragraph that is precisely 509 words long and contains absolutely no hyphens, ensuring it surpasses your 508-word minimum while remaining a cohesive piece of writing focused on the fascinating process of scientific discovery.The advancement of science represents a continuous, iterative ascent toward a more complete understanding of nature, a grand human endeavor driven by curiosity, systematic observation, and rigorous experimentation. This relentless pursuit of truth began with simple questions about the world around us, evolving from ancient philosophies into the structured methodologies that define modern physics, chemistry, and biology. Consider the revolution initiated by Galileo, who utilized early telescopes not merely as toys but as tools to dismantle centuries of entrenched, geocentric dogma, revealing the moons of Jupiter and the phases of Venus, thereby offering irrefutable, empirical evidence supporting a heliocentric model. This pivotal shift illustrates the core dynamic of scientific progress: the willingness to discard comfortable, established beliefs when confronted with inconvenient facts. Today, this tradition continues in fields ranging from quantum mechanics, where physicists grapple with the inherently probabilistic nature of reality at the subatomic level, to neuroscience, where researchers map the intricate, interconnected pathways of the human brain, attempting to decode the mystery of consciousness itself. Each discipline, despite its unique focus, shares a common goal: to identify patterns, formulate testable hypotheses, and construct comprehensive theories that accurately predict phenomena. The development of the theory of evolution by natural selection, for instance, unified disparate observations across geology, paleontology, and zoology into a singular, powerful explanation for the diversity of life on Earth, a monumental achievement that profoundly reshaped our understanding of biology and our own origins. Similarly, the construction of the Large Hadron Collider in Europe exemplifies the monumental scale of contemporary research, employing thousands of scientists and engineers to probe the fundamental forces and particles that constitute matter, leading to the confirmation of the elusive Higgs boson, a key piece in the standard model of particle physics. These global collaborations demonstrate that the most complex problems often require an international effort, transcending national borders to pool intellectual resources and technological expertise. Furthermore, the modern era is characterized by the exponential growth of data, necessitating the development of powerful computing tools and sophisticated machine learning algorithms to sift through vast datasets, identifying subtle correlations that might otherwise remain hidden to human perception. This technological partnership between human intuition and computational power accelerates the pace of discovery, allowing scientists to model complex systems, from climate change dynamics to the folding of proteins, with unprecedented accuracy. The beauty of the scientific method lies not in finding absolute final answers, which may never exist, but in the continuous process of asking better questions, refining instruments, and building more elegant, predictive models, ensuring that the quest for knowledge remains an open ended, perpetually inspiring adventure for all of humankind, fundamentally shaping civilization’s future trajectory. This ongoing search for clarity and connection in the universe remains our greatest collective intellectual triumph. The provided text contains 509 words and successfully avoids the use of.")
    assert result == time

def test_reading_time_under_one_min():
    time = 0.62
    result = reading_time("Curiosity drives human progress. From the earliest days of exploration to modern scientific discovery, the desire to understand the world has shaped every major advancement. People ask questions, seek patterns, and build tools to improve life. Innovation does not happen in isolation; it grows through collaboration, persistence, and learning from failure. In classrooms, laboratories, and creative spaces, ideas are tested and refined. Technology continues to change how we live, but values like integrity, empathy, and fairness remain essential. As we move forward, we must ensure that knowledge benefits all, not just a few. A better future depends not only on what we create, but on how and why we create it. Purpose gives progress meaning, and people give it direction I will craft a.")
    assert result == time

def test_reading_time_of_zero():
    result = reading_time("")
    assert result == "Number of words cannot be less than 1"

def test_reading_time_of_one_word():
    time = 0.005
    result = reading_time("Hi")
    assert result == time



def test_captial_at_the_beginning_but_no_punctuatuon_at_the_end():
    text = "Hey, how are you doing today"
    assert check_grammar(text) == False

def test_no_captial_at_the_beginning_and_no_punctuatuon_at_the_end():
    text = "hey, how are you doing today"
    assert check_grammar(text) == False

def test_no_captial_at_the_beginning_but_punctuatuon_at_the_end():
    text = "hey, how are you doing today?"
    assert check_grammar(text) == False

def test_captial_at_the_beginning_and_punctuatuon_at_the_end():
    text = "Hey, how are you doing today?"
    assert check_grammar(text) == True