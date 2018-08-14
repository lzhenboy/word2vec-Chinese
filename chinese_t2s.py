import os, sys
import logging
from optparse import OptionParser
from opencc import OpenCC

def zh_t2s(infile, outfile):
    '''convert the traditional Chinese of infile into the simplified Chinese of outfile'''

    # read the traditional Chinese file
    t_corpus = []
    with open(infile,'r',encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '').replace('\t','')
            t_corpus.append(line)
    logger.info('read traditional file finished!')

    # convert the t_Chinese to s_Chinese
    cc = OpenCC('t2s')
    s_corpus = []
    for i,line in zip(range(len(t_corpus)),t_corpus):
        if i % 1000 == 0:
            logger.info('convert t2s with the {}/{} line'.format(i,len(t_corpus)))
        # s_corpus.append(OpenCC.convert(line))
        s_corpus.append(cc.convert(line))
    logger.info('convert t2s finished!')

    # write the simplified Chinese into the outfile
    with open(outfile, 'w', encoding='utf-8') as f:
        for line in s_corpus:
            f.writelines(line + '\n')
    logger.info('write the simplified file finished!')


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    logger.info('running ' + program + ' : convert Traditional Chinese to Simplified Chinese')

    parser = OptionParser()
    parser.add_option('-i','--input',dest='input_file',default='corpus.zhwiki.txt',help='traditional file')
    parser.add_option('-o','--output',dest='output_file',default='corpus.zhwiki.simplified.txt',help='simplified file')
    (options,args) = parser.parse_args()

    input_file = options.input_file
    output_file = options.output_file

    try:
        zh_t2s(infile=input_file,outfile=output_file)
        logger.info('Traditional Chinese to Simplified Chinese Finished')
    except Exception as err:
        logger.info(err)




