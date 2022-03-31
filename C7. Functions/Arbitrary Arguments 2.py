# To accept any number of keyword arguments, use an argument that starts with **.

import html


def make_element(name, value, **attrs):  # attrs is a dictionary that holds the passed keyword arguments (if any).
    keyvals = [' %s = "%s"' % item for item in attrs.items()]    # key + value
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name = name, 
                                                       attrs = attr_str, 
                                                       value = html.escape(value))

    return element     


if __name__ == '__main__':    
    result = make_element('item', 'Albatross', size = 'large', quantity = 6)  
    print(result)     # print <item size="large" quantity="6">Albatross</item>
    
    result = make_element('p', '<spam>')   # print <p>&lt;spam&gt;</p>
    print(result)





