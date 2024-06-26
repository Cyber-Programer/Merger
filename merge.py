#!/usr/bin/env python
import argparse
import os

def main():
    # Example usage
    example = """
    To use this tool just follow the instructions.
    Example Usage:

        Get Help     ->    python merge.py --help
        Merge Files  ->    python merge.py -f file1.txt file2.txt
        Merge Texts  ->    python merge.py -t text1,text2 text1,text2
        Symbol       ->    python merge.py -f file1 file2 -sy :
        Symbol       ->    python merge.py -t file1 file2 -sy :
        Output       ->    python merge.py -t file1 file2 -sy - -o output.txt
            
    """

    # Create the argument parser
    parser = argparse.ArgumentParser(
        prog='merge',
        description='Merge any files/texts with any symbol.',
        epilog='''Enjoy using this tool! This tool is simple but sometimes it helps you to accomplish difficult tasks. Feel free to explore its capabilities.''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Add arguments
    parser.add_argument('-f', '--files', action="store", nargs=2, help="Input All File's Name")
    parser.add_argument('-t', '--texts', action="store", nargs=2, help="Input All Text's")
    parser.add_argument('-sy', '--symbols', action="store", help="Input the symbol you would like to include", default=':')
    parser.add_argument('-o', '--output', action="store", help="Output file to save the merged result")

    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        parser.error(example)

    parser.usage = example

    if not args.files and not args.texts:
        print(example)
    else:
        if args.texts and args.files:
            print("\nDear User, you can't use (-f) and (-t) at the same time.\n")
        elif args.texts:
            try:
                first = []
                second = []
                usrVa1, usrVa2 = args.texts
                for us1 in usrVa1.split(','):
                    first.append(us1)
                for us2 in usrVa2.split(','):
                    second.append(us2)
                
                merged_output = []
                for x, y in zip(first, second):
                    merged_output.append(f"{x}{args.symbols}{y}")
                
                output = '\n'.join(merged_output)
                
                if args.output:
                    with open(args.output, 'w') as f_out:
                        f_out.write(output)
                else:
                    print(output)
            except Exception as e:
                print(e)
        elif args.files:
            try:
                first = []
                second = []
                file1, file2 = args.files
                if os.path.exists(file1) and os.path.exists(file2):
                    with open(file1, 'r') as f1:
                        data1 = f1.readlines()
                    with open(file2, 'r') as f2:
                        data2 = f2.readlines()
                    for x in data1:
                        if x.strip():
                            first.append(x.strip())
                    for y in data2:
                        if y.strip():
                            second.append(y.strip())
                    
                    merged_output = []
                    for x, y in zip(first, second):
                        merged_output.append(f'{x}{args.symbols}{y}')
                    
                    output = '\n'.join(merged_output)
                    
                    if args.output:
                        with open(args.output, 'w') as f_out:
                            f_out.write(output)
                    else:
                        print(output)
                else:
                    print("Can't find files.")
            except Exception as e:
                print(e)
