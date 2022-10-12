# import model_Lec_4

import model_mult as model
import view

#кнопка

# def button_click():
#     value_a = view.get_value()
#     value_b = view.get_value()
#     model_Lec_4.init(value_a, value_b)
#     result = model_Lec_4.sum()
#     view.view_data(result)

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result)
