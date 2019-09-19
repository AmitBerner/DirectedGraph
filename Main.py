
import Texel_File_Format
import ParseUtil
import Graph_Handler
import Messages as msg


def main():
    """ reading the file row by row into a list """
    file_name = input(msg.ENTER_FILE_MSG)
    texel_parser = ParseUtil.Parser(Texel_File_Format.read_file)
    rules = texel_parser.read_file(file_name)

    """ creating the graph """
    rules_graph = Graph_Handler.GraphHandler(rules)

    """ printing options menu """
    print_menu(rules_graph)


def print_menu(gh: Graph_Handler):
    menu = {'1': gh.print_paths, '2': gh.print_immediate}
    while True:
        print("%s\n%s\n%s" % (msg.MENU_HEADLINE, msg.MENU_OPTION_1, msg.MENU_OPTION_2))
        choice = input()
        try:
            if choice == '0':
                return
            menu[choice]()
        except KeyError:
            print("input invalid try again!")
        print('')


if __name__ == '__main__':
    main()
