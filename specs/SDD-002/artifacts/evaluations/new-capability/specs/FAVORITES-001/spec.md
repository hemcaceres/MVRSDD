# FAVORITES-001 — Guardar favoritos de la lista

## Origen y necesidad

Solicitud exacta del fixture: «Quiero guardar favoritos de mi lista para volver a ellos.» Contexto leído: lista local para una persona; sin proveedor ni datos reales. No hay contrato previo que cubra favoritos.

## Propuesta de alcance y exclusiones

Proponer marcar y desmarcar elementos existentes como favoritos y consultar los favoritos para volver al elemento de origen. Proponer conservar la selección al cerrar y abrir el producto. Estos detalles son propuesta, no acuerdos atribuidos al usuario.

Excluir cuentas, sincronización entre dispositivos, colaboración, proveedores externos y cambios de contenido de los elementos.

## Comportamiento y aceptación propuestos

- AC-001: dada una lista con A y B sin favoritos, marcar A y consultar favoritos devuelve sólo A, conservando la lista de origen. Comprobación prevista: interacción real mediante la entrada de producto que se acuerde, seguida de consulta de datos representativos. Guardar pasos y salida; si se acuerda UI, conservar secuencia real bajo artifacts/ con viewport y estado.
- AC-002: con A favorito, desmarcar A y consultar favoritos deja la colección vacía sin eliminar A de la lista de origen. Comprobación prevista: marcar/desmarcar/consultar en la entrada real, con observaciones de cada paso y artefacto de salida o secuencia de UI pertinente.
- AC-003: con A favorito, cerrar y volver a abrir el producto conserva A como favorito. Comprobación prevista: dos ejecuciones independientes sobre los mismos datos sintéticos, registrando cierre/reapertura y consultas. Depende de acordar persistencia e identidad; no hay método ni comando ejecutable inventado.

## Diseño y decisiones a consultar

Usar identidad estable del elemento y asociación de favoritos separada de su contenido. Falta conocer cómo se implementa/accede a la lista, sus identificadores y el mecanismo de persistencia disponible. Antes de código: confirmar si la conservación entre sesiones propuesta es necesaria, cuál es la entrada existente de la lista y qué ocurre cuando un elemento favorito deja de existir. No seleccionar stack, proveedor o mecanismo de almacenamiento sin esos datos; no hubo intervención de Architect ni decisión nueva tomada.

## Aprobación del contrato

Sin aprobación. La solicitud autoriza preparación y discovery del caso, no implementar esta propuesta. Presentar este borrador y las preguntas anteriores al usuario del caso. Estado y siguiente acción sólo en [catálogo](../index.md).
