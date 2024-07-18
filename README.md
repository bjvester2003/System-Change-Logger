Use this script to log any changes or downloads made to this system. Provide the type 
of change ['Installation', 'Uninstallation', 'Configuration', or 'Other'], the        
location, wither the filepath or the menu path, and a short description of the change.
Note that this script will throw an error if the type is not from the above list.     
Additionally, the descriptions can be no longer than 150 characters. Should this limit
be exceeded a further error will be shown.

positional arguments:
  Type         The type of change being made. Changes should be from the following    
               list: ['Installation', 'Uninstallation', 'Configuration', or 'Other']  
  Location     The location of the committed change. Follow the standard X>Y>Z format 
               when supplying the location.
  Description  This is a short description of what this change entails. The length of 
               this description is locked at 150 characters.

options:
  -h, --help   show this help message and exit