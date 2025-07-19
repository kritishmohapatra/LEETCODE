class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans=[]
        for fl in folder:
            if not ans:
                ans.append(fl)
            else:
                prev_file=ans[-1]
                if fl.startswith(prev_file) and len(fl)>len(prev_file) and fl[len(prev_file)]=="/":
                    continue

                else:
                    ans.append(fl)
        return ans