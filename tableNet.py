import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.backend as K
from tensorflow import keras as keras
from tensorflow.keras.models import Model
from tensorflow.keras.applications import VGG19
from tensorflow.keras.layers import (Add, Conv2D, Conv2DTranspose, Dropout,
                                     Input)


def build_table_mask(inputs,pool4,pool3):
    X_ = Conv2D(512,(1,1),padding='same',name='conv7_table')(inputs)
    X_ = Conv2DTranspose(512,(3,3),strides=(2,2),padding='same',name='2x_conv7_table')(X_)
    X_ = Add()([X_,pool4])
    X_ = Conv2DTranspose(256,(3,3),strides=(2,2),padding='same',name='2x_conv7_table_with_pool4')(X_)
    X_ = Add()([X_,pool3])
    X_ = Conv2DTranspose(128,(3,3),strides=(2,2),padding='same')(X_)
    X_ = Conv2DTranspose(64,(3,3),strides=(2,2),padding='same')(X_)
    X_ = Conv2DTranspose(6,(3,3),strides=(2,2),padding='same')(X_)
    X_ = Conv2DTranspose(3,(3,3),strides=(1,1),padding='same')(X_)

    return X_
    
def build_column_mask(inputs,pool4,pool3):
    X_ = Conv2D(512,(1,1),padding='same',name='conv7_column',activation='relu')(inputs)
    X_ = Dropout(0.8)(X_)
    X_ = Conv2D(512,(1,1),padding='same',name='conv8_column')(X_)
    X_ = Conv2DTranspose(512,(3,3),strides=(2,2),padding='same',name='2x_conv8_column')(X_)
    X_ = Add(name='Add_2conv8_pool4')([X_,pool4])
    X_ = Conv2DTranspose(256,(3,3),strides=(2,2),padding='same',name='2x_Add_2conv8_pool4')(X_)
    X_ = Add(name='Add_with_pool3')([X_,pool3])
    X_ = Conv2DTranspose(128,(3,3),strides=(2,2),padding='same')(X_)
    X_ = Conv2DTranspose(64,(3,3),strides=(2,2),padding='same')(X_)
    X_ = Conv2DTranspose(6,(3,3),strides=(2,2),padding='same')(X_)
    X_ = Conv2DTranspose(3,(3,3),strides=(1,1),padding='same')(X_)
    
    return X_

def tableNetModel():
    input_tensor = Input(shape=(1024,1024,3))
    base_model = VGG19(include_top=False,input_tensor=input_tensor,weights='imagenet')
    X = Conv2D(512,(1,1),activation='relu',name='conv6_with_dropout_1',padding='same')(base_model.output)
    X = Dropout(0.8)(X)
    X = Conv2D(512,(1,1),activation='relu',name='conv6_with_dropout_2',padding='same')(X)
    X = Dropout(0.8)(X)

    table_output = build_table_mask(X,base_model.get_layer('block4_pool').output,base_model.get_layer('block3_pool').output)
    column_output = build_column_mask(X,base_model.get_layer('block4_pool').output,base_model.get_layer('block3_pool').output)

    tableNet = Model(inputs = input_tensor, outputs=[table_output,column_output],name='tableNet')
    return tableNet


if __name__ == '__main__':
    tableNetModel()
