import os, sys
import logging
from optparse import OptionParser
import re


def remove_en_blank(infile,outfile):
    '''remove the english word and blank from infile, and write into outfile'''
    with open(infile,'r',encoding='utf-8') as fin, open(outfile,'w',encoding='utf-8') as fout:
        relu = re.compile(r'[ a-zA-Z]')  # delete english char and blank
        i = 0
        for line in fin:
            res = relu.sub('', line)
            fout.write(res)
            i += 1
            if i % 1000 == 0:
                logger.info('handing with the {} line'.format(i))


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger.info('running ' + program + ': remove english and blank')

    # parse the parameters
    parser = OptionParser()
    parser.add_option('-i','--input',dest='infile',default='corpus.zhwiki.simplified.txt',help='input file to be preprocessed')
    parser.add_option('-o','--output',dest='outfile',default='corpus.zhwiki.simplified.done.txt',help='output file removed english and blank')
    (options,args) = parser.parse_args()

    infile = options.infile
    outfile = options.outfile

    try:
        remove_en_blank(infile, outfile)
        logger.info('remove english and blank finished')
    except Exception as err:
        logger.info(err)
