from os import system

def main(path, password):
        usr = "root@"
        with open("conf.txt") as fp:
                source = usr+fp.readline().split("-")[0]+path+"vaqa.tar"
                for agent_entry in fp:
                        agent = agent_entry.split("-")[0]
                        cmd = "scp " + source + " " + usr+agent+path
                        print cmd
                        #system(cmd)
                        break
                        
if __name__ == "__main__":
        path = ":/opt/"
        password = "ssl12345"
        main(path, password)
