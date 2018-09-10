from behave import *
from src.cotizador import *

def before_scenario(context, scenario):
	context = {}

@given("que la ciudad del cliente es {ciudad}")
def step_impl(context,ciudad):
	context.ciudad = ciudad

@given("que la edad del cliente es {edad}")
def step_impl(context,edad):
	context.edad = int(edad)

@given("que el genero del cliente es {genero}")
def step_impl(context,genero):
	context.genero = genero

@given("que el estado civil del cliente es {estado}")
def step_impl(context,estado):
	context.estado = estado

@given("que el cliente tiene pre-existencia {preexistencias}")
def step_impl(context,preexistencias):
	context.preexistencias = preexistencias

@given("que el cliente tiene {dependientes} dependientes")
def step_impl(context,dependientes):
	context.dependientes = int(dependientes)

@when("solicite la cotizacion")
def step_impl(context):
	context.resultado = cotizar_seguro(context.ciudad, context.edad, context.genero, context.estado, context.preexistencias, context.dependientes)

@then("obtiene el mensaje '{message}'")
def step_impl(context, message):
	assert context.resultado == message