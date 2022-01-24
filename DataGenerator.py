from AccessLog.AccessData import accessCVS
from Friend.FriendData import generateFriendsCSV
from MyPage.MyPageData import generateMyPageCSV

if __name__ == '__main__':
    generateMyPageCSV()
    generateFriendsCSV()
    accessCVS()