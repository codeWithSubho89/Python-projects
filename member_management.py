from file_handling import load_file, save_file

class Member:
    def __init__(self):
        self.MEMBERS_File = 'data/members.json'

    def add_member(self):
        members = load_file(self.MEMBERS_File)
        member_id = input("Enter member id: ").strip().upper()
        
        for member in members:
            if not member["member_id"] == member_id:
                name = input("Enter member's name: ").strip()
                email = input("Enter member's email: ").strip()
                if not name == "" or email == "":
                    members.append({
                        "member_id": member_id,
                        "name": name,
                        "email": email,
                        "isActive": "Active"
                    })
                    save_file(self.MEMBERS_File,members)
                    print("member added !!!")
                    return
                else:
                    print("All fields are required!")
                    return
            else:
                print("Member already registered...")
    
    def disply_member(self):
        members = load_file(self.MEMBERS_File)
        print("---------------------LIST OF MEMEBERS---------------------------------")
        print("----------------------------------------------------------------------")
        print("ID-------------NAME------------EMAIL------------------STATUS")
        for member in members:
            print(f"{member["member_id"]}----------{member["name"]}----------{member["email"]}---------{member["isActive"]}")

    def deAcivate_member(self):
        members = load_file(self.MEMBERS_File)
        member_id = input("Enter member ID: ").strip().upper()
        for member in members:
            if member["member_id"] == member_id:
                if member["isActive"] == "Active":
                    member["isActive"] = "DeActive"
                    save_file(self.MEMBERS_File,members)
                    print("Member status updated...")
                    return
                else:
                    print("Member already DeActived...")
                    ask = input("Do you want to active the status....(Y/N): ").strip().lower()
                    if ask == 'y':
                        member["isActive"] = "Active"
                        save_file(self.MEMBERS_File,members)
                        print("Member status updated...")
                        return
                    else:
                        print("update cancel....")
                        return
        print("Invaild member ID...")

    def delete_member(self):
        members = load_file(self.MEMBERS_File)
        member_id = input("Enter member ID: ").strip().upper() 
        for member in members:
            if member["member_id"] == member_id:
                ask = input("Are you sure you want to delete? (Y/N): ").lower()
                if ask == 'y':
                    members.remove(member)
                    save_file(self.MEMBERS_File, members)
                    print("Member removed from library!")
                else:
                    print("Deletion cancelled.")
                return
        
        print("invalid ID")       
               
               
            
                
