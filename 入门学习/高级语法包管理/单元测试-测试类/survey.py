class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self,question):
        """存储一个问题，并为存储的答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self,new_response):
        """存储单份调查答案"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for response in self.responses:
            #这个是对单个回答的打印，可以加-
            #print('- '+response)
            ###对一个人对各回答的就不能添加'-'再进行+
            print('-',response)









