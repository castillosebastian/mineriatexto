def concatenate_text_files(corpus_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for fname in os.listdir(corpus_path):
            if fname.endswith('.txt'):
                fpath = os.path.join(corpus_path, fname)
                with open(fpath, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        outfile.write(line)
    print(f"All text files in {corpus_path} have been concatenated into {output_file}.")

concatenate_text_files('/home/sebacastillo/mineriatexto/data/corpus/borges/', '/home/sebacastillo/mineriatexto/data/borges_combined.txt')