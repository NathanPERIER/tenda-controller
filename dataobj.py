
class DataObject :

	def loadDict(self, data: "dict[str,any]") :
		for k in self.__dict__ :
			self.__dict__[k] = data[k]

	def __getitem__(self, item: str) -> any :
		return self.__dict__[item]

	def getDict(self) -> "dict[str,any]" :
		return self.__dict__
