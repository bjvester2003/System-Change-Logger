import argparse as ap
import sys
import datetime as dt
import os

def get_arguments():
    """Initializes the parser and retrieves arguments from the command line"""
    
    parser = ap.ArgumentParser(prog="System Change Logger", description="Use this script to log any changes or downloads made to this system. Provide the type of change ['Installation', 'Uninstallation', 'Configuration', or 'Other'], the location, wither the filepath or the menu path, and a short description of the change. Note that this script will throw an error if the type is not from the above list. Additionally, the descriptions can be no longer than 150 characters. Should this limit be exceeded a further error will be shown.", epilog='')
    
    parser.add_argument("Type", help="The type of change being made. Changes should be from the following list: ['Installation', 'Uninstallation', 'Configuration', or 'Other']")
    parser.add_argument("Location", help="The location of the committed change. Follow the standard X>Y>Z format when supplying the location.")
    parser.add_argument("Description", help="This is a short description of what this change entails. The length of this description is locked at 150 characters.")
    
    return parser.parse_args()
        
def strip_args(args):
    """Strips argument data to include only necessary data."""
    
    return {
        "Type" : (args.Type).strip("Type="),
        "Location" : (args.Location).strip("Location="),
        "Description" : (args.Description).strip("Description=")}
    
def check_arguments_valid(arg_data):
    """Ensures that argument type is valid and description length is not excessive."""
    
    if arg_data["Type"] not in ['Installation', 'Uninstallation', 'Configuration', 'Other']:
        sys.exit("\n##### ERROR : Invalid type. #####")
    elif len(arg_data["Description"]) > 150:
        sys.exit("\n##### ERROR : Description length exceeded. #####")   
    
def get_day_change_made():
    """Retrieves the timestamp of the change report."""
    
    current_date = dt.datetime.now()
    current_date = current_date.strftime("%c")
    
    return current_date

def write_information_to_file(change_data):
    """Writes information to a .log file."""
    
    writepath = './changes.log'
    mode = 'a' if os.path.exists(writepath) else 'w'
    
    with open(writepath, mode) as log_file:
        line = f"{change_data['Date']}, {change_data['Type']}, {change_data['Location']}, {change_data['Description']}"
        
        if mode == 'a':
            log_file.write("\n"+line)
        else:
            log_file.write(line)
    log_file.close()
    
def main():
    args = get_arguments()
    change_data = strip_args(args)
    check_arguments_valid(change_data)
    change_data["Date"] = get_day_change_made()
    write_information_to_file(change_data)

if __name__ == "__main__":
    main()