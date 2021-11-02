from io import TextIOWrapper
import logging, sys, copy, yaml, ast

class Task:

    def __init__(self, task, name=None):
        self.task = task
        self.parameters = []
        self.results = []
        self.description = ''
        self.steps = []

        if name:
            self.name = name
        else: 
            self.name = self.task['metadata']['name']

        self._get_parameters()
        self._get_results()
        self._get_description()
        self._get_steps()
        
        
    def _get_parameters(self):
        if 'params' in self.task['spec']:
            self.parameters = self.task['spec']['params']
    
    def get_parameters(self):
        return self.parameters

    def _get_description(self):
        if 'description' in self.task['spec']:
            self.description = self.task['spec']['description']
    
    def get_description(self):
        return self.description

    def _get_results(self):
        if 'results' in self.task['spec']:
            self.results = self.task['spec']['results']
    
    def get_results(self):
        return self.results

    def _get_steps(self):
        if 'steps' in self.task['spec']:
            self.steps = self.task['spec']['steps']

    def get_steps(self):
        return self.steps

    def _write_parameters_markdown(self, f: TextIOWrapper):
        if self.parameters == []:
            return
        f.write("### Parameters\n")
        for p in self.parameters:
            f.write("* {}\n".format(p['name']))
            if 'description' in p:
                f.write("\t* description: {}\n".format(p['description']))
            if 'default' in p:
                if p['default'] == '':
                    f.write("\t default: ''\n")
                else:
                    f.write("\t default: {}\n".format(p['default']))
            if 'type' in p:
                f.write("\t type: {}\n".format(p['type']))
    
    def _write_results_markdown(self, f: TextIOWrapper):
        if self.results == []:
            return
        f.write("### Results\n")
        for r in self.results:
            f.write("* {}\n".format(r['name']))
            if 'description' in r:
                f.write("\t* description: {}\n".format(r['description']))
    
    def _write_steps_markdown(self, f: TextIOWrapper):
        if self.steps == []:
            return
        f.write("## Steps\n")
        for s in self.steps:
            f.write("#### {}\n".format(self.s['name']))
            if 'image' in s:
                f.write("Image used: {}\n".format(s['image']))
            if 'env' in s:
                f.write("Environment variables:\n")
                for e in s['env']:
                    f.write("* {}\n".format(e['name']))
                    if 'value' in e:
                        f.write("\tValue: {}\n".format(e['value']))
                    elif 'valueFrom' in e and 'secretKeyRef' in e['valueFrom']:
                        f.write("\tValue from secret: {}\n".format(e['valueFrom']['secretKeyRef']['name']))

    def self_document_markdown(self, filename):
        with open(filename, 'w') as f:
            f.write("#Overview\n")
            if self.description != '':
                f.write("##Description\n")
                f.write(self.description + '\n')
            f.write("## Parameters and Results\n")
            self._write_parameters_markdown(f)
            self._write_results_markdown(f)
            self._write_steps_markdown(f)

            