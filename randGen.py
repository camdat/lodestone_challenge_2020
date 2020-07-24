import random
import datetime

class Generator:
    """ 
    Generator generates random rows of data based on 
    ranges defined at either initialization or call time
    this allows it to be very flexible and able to generate
    rows of many types

    Attributes
    ----------
    date_tup: optional
        defines the date range to be generated within.

    **labels: optional
        optional additonal labels to randomize between.
        
        in the case of Lodestone's requirements, these are key/value
        pairs which define rater score, correct/rater answers, etc. 
        an example usage based on those requirements is given below

    Methods
    -------
    __gen_date: private
        generates a random datetime.datetime object from given datetime range

    __gen_lab: private
        picks a random element from an input list

    __gen_num: private
        generates a randome number from given range

    gen_row: public
        generates a row from either initalized or given variables

    gen_n_rows: public
        generates n rows of the given pattern, with id fields

    Examples
    --------

    Define ranges at calltime:
        g = Generator()
        g.gen_row((datetime.datetime(2005, 10, 1), datetime.datetime(2005, 11, 2), a=['A', 'B', 'C']

        returns: {'date': datetime.datetime(2005, 10, 2, 21, 56, 16), 'a':'B'}

    Define ranges at initialization:
        date_range = (datetime.datetime(2005, 10, 1), datetime.datetime(2005, 10, 30))
        rater_score = ['A', 'B', 'C', 'D', 'E']
        answer_3 = ['Low', 'Average', 'High']
        answer_5 = ['Bad', 'Okay', 'Intermediate', 'Great', 'Exceptional']


        g = Generator(seed=None, date_tup=date_range, cor_3=answer_3, cor_5=answer_5, rater_3=answer_3, rater_5=answer_5)
        g.gen_row()

        returns: {'date': datetime.datetime(2005, 10, 2, 21, 56, 16), 'cor_3': 'High', 'cor_5': 'Great', 'rater_3': 'Average', 'rater_5': 'Exceptional'}

    """
   
    
    def __init__(self, seed=None, date_tup=None, **labels):
        self.rand = random.Random(seed)
        self.date_tup = date_tup
        self.labels = labels

    def __gen_date(self, start:datetime.datetime, end:datetime.datetime) -> datetime.datetime:
        # we can convert the float timestamp values to int without
        # loss of precision because we only want day-level granularity
        rand_date = self.__gen_num(int(start.timestamp()), int(end.timestamp()))
        return datetime.datetime.fromtimestamp(rand_date)

    def __gen_lab(self, in_list:list) -> str:
        return self.rand.choice(in_list)

    def __gen_num(self, start:int, end:int) -> int:
        return self.rand.randint(start, end)

    def gen_row(self, date_tup=None, id_num=None, **labels) -> dict:
        # check if we should use initialized or current vars
        date_tup = date_tup if date_tup else self.date_tup
        labels = labels if labels else self.labels

        if date_tup is None:
            return None

        output = {}

        output["date"] = self.__gen_date(date_tup[0], date_tup[1]).strftime("%m-%d-%Y")
        if id_num:
            output["id"] = str(id_num)

        # pick a random label for each input **labels
        for key, label in labels.items():
            output[key] = self.__gen_lab(label)
        return output

    def gen_n_rows(self, num, date_tup=None, **labels) -> list:
        output = []
        for i in range(1, num+1):
            output.append(self.gen_row(id_num=i, date_tup=date_tup, **labels))
        return output

