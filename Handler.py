import os, csv
from DataTypes.ObjectType import ObjectType
from DataTypes.Collection import Collection
from DataTypes.Library import Library
import InputManager, OutputManager, OutputManager2
from Comparators.NumberComparator import NumberComparator
from Comparators.LetterComparator import LetterComparator
from Comparators.BooleanComparator import BooleanComparator
from SortingAlgorithms.Quicksort import Quicksort
from math import fabs


class Handler:

    def __init__(self):

        # This is the default Directory where libraries are saved
        self.dir_path = "C:/Users/irixa/PycharmProjects/GODA/Directory"
        self.libraries = {}
        #self.collections = {}
        self.objects = {}


    def openLibrary(self, library_name):
        """
        Creates an instance of a library so that a user can
        use commands to manage it
        :param library_name: str - library name
        :return: None
        """

        if self.library_is_opened(library_name):
            print("Library %s is already opened" % library_name)
            return
        #library = InputManager.imp_new_library(library_name)
        self.libraries[library_name] = Library(library_name)



    def close_library(self, library_name):
        """
        Deletes the instance of an opened library
        :param library_name: str - library name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or it is not opened" % library_name)
            return
        del self.libraries[library_name]


    def library_is_opened(self, library_name):
        for key in self.libraries:
            if key == library_name:
                return True
        return False


    def create_library(self, library_name):
        """
        Creates a new library
        :param library_name: str - library name
        :return: None
        """
        #library = Library(library_name)
        OutputManager2.create_library(self.dir_path, library_name)
        #OutputManager.save_library(library)
        self.openLibrary(library_name)


    def create_collection(self, library_name, collection_name, object_type):
        """
        Creates a new collection and adds it to a library
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param object_type: str - name of the object type
        :return:
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return

        lib = self.libraries[library_name]
        obj_type = self.objects[object_type]
        col = Collection(collection_name, obj_type)
        lib.add_collection(col)
        OutputManager2.create_collection(self.dir_path, library_name, col)


    def create_object(self, obj_name, obj_attributes):
        """
        Creates a new object
        :param obj_name: str - object name
        :param obj_attributes: dictionary of object attributes
        :return: None
        """
        obj = ObjectType(obj_name, obj_attributes)
        self.objects[obj_name] = obj


    def add_object(self, library_name, collection_name, arr):
        """
        Adds an object to a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param arr: array - object values
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)
        col.add_obj(arr)
        OutputManager2.add_object_to_collection("{}/{}/Collections/{}.csv".format(self.dir_path, library_name, collection_name), arr)


    def remove_library(self, library_name):
        """
        Deletes a library
        :param library_name: str - library name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        OutputManager2.delete_library(self.dir_path + "/" + library_name)
        del self.libraries[library_name]


    def remove_collection_from_library(self, library_name, collection_name):
        """
        Deletes a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        lib.remove_collection(collection_name)
        OutputManager2.delete_collection(self.dir_path + "/" + library_name, collection_name)


    def remove_object_from_collection(self, library_name, collection_name, index):
        """
        Removes an object from a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param index: int - index of the object to be removed
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)
        if index >= col.col_size():
            print("An object with index %s does not exist" % index)
            return
        col.remove_obj(index)
        OutputManager2.delete_collection(self.dir_path + "/" + library_name, collection_name)
        OutputManager2.create_collection(self.dir_path, library_name, col)

    def sort(self, library_name, collection_name, attribute_name):
        """
        Sorts a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param attribute_name: str - attribute to which the collection will be sorted
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)
        obj = col.get_obj_def()
        attr = obj.get_obj_attributes()

        # Get the attribute index in the object array
        index = -1
        for a in range(len(attr)):
            if attr[a] == attribute_name:
                index = a
                break
        if index == -1:
            print("Attribute %s does not exist." % attribute_name)
            return

        # Create comparator according to the attribute data type
        data_type = obj.get_obj_data_types()[index]\
        # Data type is a string
        if isinstance(data_type, str):
            comp = LetterComparator()
        # Data type is either an int or a float
        elif isinstance(data_type, int) or isinstance(data_type, float):
            comp = NumberComparator()
        # Data type is boolean
        elif isinstance(data_type, bool):
            comp = BooleanComparator()
        else:
            print("Error") # no se supone que ocurra este error

        data = col.get_obj_list()

        sorted_list = Quicksort().sort(data, comp, index)
        temp_collection = Collection('temp', obj)
        for o in sorted_list:
            temp_collection.add_obj(o.get_values())
        col = temp_collection
        del temp_collection
        col.display_col()
        #OutputManager.export_collection(col)



    def search_in_collection(self, library_name, collection_name, attribute_name, data_to_search):
        """
        Search for objects with a given parameter in a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param attribute_name: str - attribute name
        :param data_to_search: data that the user wishes to search
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)

        attr = col.get_obj_def().get_obj_attributes()
        # Get the attribute index in the object array
        index = -1
        for a in range(len(attr)):
            if attr[a] == attribute_name:
                index = a
                break
        if index == -1:
            print("Attribute %s does not exist." % attribute_name)
            return

        data = col.get_obj_list()
        result = []
        for obj in data:
            if obj.get_value(index) == data_to_search:
                result.append(obj)

        temp_collection = Collection('temp', col.get_obj_def())
        for o in result:
            temp_collection.add_obj(o.get_values())
        temp_collection.display_col()
        del temp_collection


    def search_in_library(self):
        # What does this do?
        pass


    def show_library(self, library_name):
        """
        Shows all the collection names in a library
        :param library_name: str - library name
        :return:
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        library = self.libraries[library_name]
        library.display_lib()


    def show_collection(self, library_name, collection_name):
        """
        Displays the data inside a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        collection = lib.get_collection(collection_name)
        collection.display_col()


    def show_all_in_library(self, library_name):
        """
        Display all the collections in a library with corresponding data
        :param library_name: str - library name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        lib.display_all_lib()


    def merge(self, lib_name1, col_name1, lib_name2, col_name2, new_col_name, lib_name3):
        """
        Merges two collections
        :param lib_name1: str - library name of collection 1
        :param col_name1: str - collection 1 name
        :param lib_name2: str - library name of collection 2
        :param col_name2: str - collection 2 name
        :param new_col_name: str - name of the new collection to be created
        :param lib1: str - library name where new collection will be saved
        :return: None
        """
        if not self.library_is_opened(lib_name1):
            print("Library %s does not exist or is not opened" % lib_name1)
            return
        if not self.library_is_opened(lib_name2):
            print("Library %s does not exist or is not opened" % lib_name2)
            return
        if not self.library_is_opened(lib_name3):
            print("Library %s does not exist or is not opened" % lib_name3)
            return

        lib1 = self.libraries[lib_name1]
        lib2 = self.libraries[lib_name2]
        lib3 = self.libraries[lib_name3]

        col1 = lib_name1.get_collection(col_name1)
        col2 = lib_name2.get_collection(col_name2)

        # Get object types
        obj1 = col1.get_obj_def()
        obj2 = col2.get_obj_def()

        # Check compatibility
        if self.is_coll_compatible(obj1, obj2):
            newCol = Collection(new_col_name, obj1)
            list1 = col1.get_obj_list()
            for obj in list1:
                newValues = []
                values = obj.get_values()
                for v in values:
                    newValues.append(v)
                newCol.add_obj(newValues)
            list2 = col2.get_obj_list()
            for obj in list2:
                newValues = []
                values = obj.get_values()
                for v in values:
                    newValues.append(v)
                newCol.add_obj(newValues)

            lib3.add_collection(newCol)

        # Not compatible
        else:
            print("Collections %s and %s are not compatible." % (col_name1, col_name2))


    # Not sure if this function is already in another class ??
    def is_coll_compatible(self, obj1, obj2):
        """
        Checks compatibility between two objects.
        That is, that all attributes are exactly the same.
        :param obj1: ObjectType - object 1
        :param obj2: ObjectType - object 2
        :return: boolean - True if objects are compatible
        """
        # Check that attribute names are the same
        attr1 = obj1.get_obj_attributes()
        attr2 = obj2.get_obj_attributes()
        if fabs(len(attr1) - len(attr2)) > 0:
            return False
        for a in range(len(attr1)):
            if attr1[a] is not attr2[a]:
                return False

        # Check that attribute types are the same
        type1 = obj1.get_obj_data_types()
        type2 = obj2.get_obj_data_types()
        for t in range(len(type1)):
            if type1[t] is not type2[t]:
                return False

        return True



    def edit_collection(self, collection_name):
        pass

    def edit_library(self, library_name):
        pass
