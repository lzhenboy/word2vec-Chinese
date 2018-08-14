import logging
import os.path
import sys
from optparse import OptionParser
from gensim.corpora import WikiCorpus


def parse_corpus(infile, outfile):
    '''parse the corpus of the infile into the outfile'''
    space = ' '
    i = 0
    with open(outfile, 'w', encoding='utf-8') as fout:
        wiki = WikiCorpus(infile, lemmatize=False, dictionary={})  # gensim中的维基百科处理类WikiCorpus
        for text in wiki.get_texts():
            fout.write(space.join(text) + '\n')
            i += 1
            if i % 10000 == 0:
                logger.info('Saved ' + str(i) + ' articles')


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(program)  # logging.getLogger(logger_name)
    logger.info('running ' + program + ': parse the chinese corpus')

    # parse the parameters
    parser = OptionParser()
    parser.add_option('-i','--input',dest='infile',default='zhwiki-latest-pages-articles.xml.bz2',help='input: Wiki corpus')
    parser.add_option('-o','--output',dest='outfile',default='corpus.zhwiki.txt',help='output: Wiki corpus')

    (options,args) = parser.parse_args()

    infile = options.infile
    outfile = options.outfile

    try:
        parse_corpus(infile, outfile)
        logger.info('Finished Saved ' + str(i) + 'articles')
    except Exception as err:
        logger.info(err)


