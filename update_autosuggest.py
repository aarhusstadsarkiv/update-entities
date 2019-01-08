    def batchInsertAutoGroup(self, data):
        updateList = []
        
        for batchDict in data:
            colID = batchDict.get("col_id")
            pType = batchDict.get("p_type")
            pData = batchDict.get("p_data")
            
            if pType == "entities":
                for eID, eDomain in pData:
                    updateList.extend(self.insertAutoGroup(eID, eDomain, colID))
            elif pType == "col_tags":
                for colTagString in pData:
                    updateList.extend(self.insertAutoColTag(colTagString, colID))
            
            del(batchDict)
        ndb.put_multi(updateList)
        del updateList


    def insertAutoGroup(self, eID, eDomain, groupID):
        modifiedList = []
            
        gqlString = u"SELECT * FROM AutoToken_v2 WHERE tokenID=%s AND tokenDomain='%s' AND autoGroup!=%s" % (eID, eDomain, groupID)
        result = ndb.gql(gqlString)
        
        for autoToken in result:
            autoGroup = set(getattr(autoToken, "autoGroup", []))
            if groupID not in autoGroup:
                autoGroup.add(groupID)
                autoToken.autoGroup = sorted(list(autoGroup))
                modifiedList.append(autoToken)
                    
        return modifiedList

if __name__ == '__main__':
    main()
