import sentencepiece as spm

# Step 1: Train tokenizer
spm.SentencePieceTrainer.train(
    input='dataset.txt',
    model_prefix='mytokenizer',
    vocab_size=340,
    model_type='bpe',   # can be 'unigram', 'char', 'bpe'
    character_coverage=0.9995
)

# Step 2: Use it
import sentencepiece as spm
sp = spm.SentencePieceProcessor(model_file='mytokenizer.model')

text = "The large language model is learning tokens!"
ids = sp.encode(text, out_type=int)
print("Token IDs:", ids)
print("Decoded:", sp.decode(ids))
