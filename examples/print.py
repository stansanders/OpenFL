#!/usr/bin/env python
"""
This is a Python script that prints an FLP
"""
import argparse
import OpenFL.Printer as P


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Print a .flp")
    parser.add_argument('input', metavar='input', type=str,
                        help='source flp file')
    args = parser.parse_args()
    print('Identifying printer...')
    p = P.Printer()
    
    p.initialize()
    print('Printer intialized...')
    p.write_block(0, args.input)
    print('Wrote block, starting printing...')
    p.start_printing(0)
    print('Done.')
