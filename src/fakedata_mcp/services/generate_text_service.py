"""Generate placeholder text."""

import random

LOREM_WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do",
    "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "enim",
    "ad", "minim", "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi",
    "aliquip", "ex", "ea", "commodo", "consequat", "duis", "aute", "irure", "in", "reprehenderit",
    "voluptate", "velit", "esse", "cillum", "fugiat", "nulla", "pariatur", "excepteur", "sint",
    "occaecat", "cupidatat", "non", "proident", "sunt", "culpa", "qui", "officia", "deserunt",
    "mollit", "anim", "id", "est", "laborum", "at", "vero", "eos", "accusamus", "iusto", "odio",
    "dignissimos", "ducimus", "blanditiis", "praesentium", "voluptatum", "deleniti", "atque",
    "corrupti", "quos", "dolores", "quas", "molestias", "recusandae", "itaque", "earum", "rerum",
    "hic", "tenetur", "sapiente", "delectus", "aut", "reiciendis", "voluptatibus", "maiores",
    "alias", "perferendis", "doloribus", "asperiores", "repellat",
]

SENTENCE_STARTERS = [
    "The quick brown fox", "In a world of possibilities", "Technology continues to",
    "According to recent findings", "Many experts believe that", "It has been observed that",
    "Research suggests that", "One could argue that", "The fundamental question remains",
    "Looking at the bigger picture", "Data shows that", "Studies have confirmed",
    "In today's landscape", "The evidence points to", "Historically speaking",
    "From a practical standpoint", "Given the circumstances", "As we move forward",
    "The key takeaway is", "Building on this foundation",
]

SENTENCE_ENDINGS = [
    "drives innovation across industries.",
    "remains a critical consideration.",
    "has significant implications for the future.",
    "continues to evolve rapidly.",
    "presents both challenges and opportunities.",
    "requires careful analysis and planning.",
    "has transformed how we approach problems.",
    "underscores the importance of adaptability.",
    "opens new avenues for growth.",
    "demands a thoughtful and measured response.",
    "shapes the trajectory of progress.",
    "highlights the need for collaboration.",
    "creates value in unexpected ways.",
    "reflects deeper structural changes.",
    "builds on decades of prior work.",
]


class GenerateText:
    """Generate placeholder text."""

    def execute(self, type: str = "lorem", count: int = 3) -> dict:
        count = max(1, min(count, 50))

        if type == "words":
            text = " ".join(random.choices(LOREM_WORDS, k=count))
        elif type == "sentences":
            sentences = []
            for _ in range(count):
                starter = random.choice(SENTENCE_STARTERS)
                ending = random.choice(SENTENCE_ENDINGS)
                sentences.append(f"{starter} {ending}")
            text = " ".join(sentences)
        elif type == "paragraphs":
            paragraphs = []
            for _ in range(count):
                num_sentences = random.randint(4, 8)
                sentences = []
                for _ in range(num_sentences):
                    starter = random.choice(SENTENCE_STARTERS)
                    ending = random.choice(SENTENCE_ENDINGS)
                    sentences.append(f"{starter} {ending}")
                paragraphs.append(" ".join(sentences))
            text = "\n\n".join(paragraphs)
        else:  # lorem
            paragraphs = []
            for i in range(count):
                words = list(LOREM_WORDS) if i == 0 else random.sample(LOREM_WORDS, k=len(LOREM_WORDS))
                chunk_size = random.randint(40, 70)
                chunk = words[:chunk_size]
                if i == 0:
                    para = "Lorem ipsum dolor sit amet, " + " ".join(chunk[5:]) + "."
                else:
                    chunk[0] = chunk[0].capitalize()
                    para = " ".join(chunk) + "."
                paragraphs.append(para)
            text = "\n\n".join(paragraphs)

        word_count = len(text.split())
        return {"text": text, "type": type, "word_count": word_count}
