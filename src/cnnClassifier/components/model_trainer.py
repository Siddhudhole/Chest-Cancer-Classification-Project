import os 
import sys 
from pathlib import Path
import tensorflow as tf 
from tensorflow import keras 
from cnnClassifier.config.configuration import ConfigurationManager 
from cnnClassifier.entity.entity_config import TrainModelConfig 




class Training:
    def __init__(self,config=TrainModelConfig):
        self.config = config


    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_trained_model_path
        )

    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            validation_split=0.20
        )

        dataflow_kawargs = dict (
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation='bilinear')
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **datagenerator_kwargs
        )
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else :
            train_datagenerator = valid_datagenerator 

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle=True,
            **dataflow_kawargs
        )

    @staticmethod
    def save_model(path:Path,model:tf.keras.Model):
        model.save(path)

    def train(self):
        self.steps_per_epoch =self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            steps_per_epoch=self.steps_per_epoch,
            epochs=self.config.params_epochs,
            validation_data=self.valid_generator,
            validation_steps=self.validation_steps
        )
        self.save_model(self.config.trained_model_path,self.model)

        