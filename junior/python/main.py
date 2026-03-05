from typing import List, Tuple, Dict, Any
import json


def check_panel_dimensions(
    panel_width: int, panel_height: int, roof_width: int, roof_height: int
) -> bool:
    result = True
    if roof_width < panel_width or roof_height < panel_height:
        result = False
    return result


def calculate_panels(
    panel_width: int,
    panel_height: int,
    roof_width: int,
    roof_height: int,
) -> int:

    # Implementa acá tu solución
    # Agregue la función auxiliar check_panel_dimensions fuera de esta función como parte de la solución pero podría haber estado incluida directamente
    # Agregue la función calculate_panels_overlap para resolver el objetivo opcional 2

    roof_area = roof_width * roof_height
    panel_area = panel_width * panel_height

    fits = check_panel_dimensions(panel_width, panel_height, roof_width, roof_height)
    fits_rotated = check_panel_dimensions(
        panel_height, panel_width, roof_width, roof_height
    )

    panels = roof_area // panel_area if fits or fits_rotated else 0

    return panels


class overlap_dict(dict):
    width: int
    height: int

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise Exception("Error accediendo a los valores de la superposición")


def calculate_panels_with_overlap(
    panel_width: int,
    panel_height: int,
    roof_width: int,
    roof_height: int,
    overlap: dict,
) -> int:
    # Se asume que el techo tiene 2 rectángulos del mismo porte superpuestos (opción 2)
    # Cree la clase overlap_dict porque prefiero acceder a los valores usando objeto.valor en lugar de objeto["valor"]

    # Decidi usar un diccionario para el overlap porque en algunos casos sus dimensiones pueden afectar el resultado
    # EJ: Si tienes un panel 1x5 y 2 rectangulos 4x2 con un overlap 1x1 puedes quedar con un width total de 5 cambiando el resultado
    # Decidí no tomar en cuenta los casos borde en los que afecte la posición de este overlap y utilizar unicamente su área por lo que el TEST 2 falla

    overlap = overlap_dict(overlap)
    overlap_width, overlap_height = overlap.width, overlap.height

    overlap_area = overlap_width * overlap_height
    Total_roof_area = roof_width * roof_height * 2 - overlap_area
    panel_area = panel_width * panel_height

    # Estos valores son condicionales y dependen del lugar del overlap los dejo definidos pero no los uso actualmente
    total_width = roof_width * 2 - overlap_width
    total_height = roof_height * 2 - overlap_height

    fits = check_panel_dimensions(panel_width, panel_height, roof_width, roof_height)
    fits_rotated = check_panel_dimensions(
        panel_height, panel_width, roof_width, roof_height
    )

    panels = Total_roof_area // panel_area if fits or fits_rotated else 0
    return panels


def run_tests() -> None:
    with open("test_cases.json", "r") as f:
        data = json.load(f)
        test_cases: List[Dict[str, Any]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"],
            }
            for test in data["testCases"]
        ]

    print("Corriendo tests:")
    print("-------------------")

    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]

        print(f"Test {i}:")
        print(
            f"  Panels: {test['panel_w']}x{test['panel_h']}, "
            f"Roof: {test['roof_w']}x{test['roof_h']}"
        )
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def run_tests_overlap() -> None:
    with open("test_cases_overlap.json", "r") as f:
        data = json.load(f)
        test_cases: List[Dict[str, Any]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "overlap": test["overlap"],
                "expected": test["expected"],
            }
            for test in data["testCases"]
        ]

    print("Corriendo tests con bonificación 2:")
    print("-------------------")

    for i, test in enumerate(test_cases, 1):
        result = calculate_panels_with_overlap(
            test["panel_w"],
            test["panel_h"],
            test["roof_w"],
            test["roof_h"],
            test["overlap"],
        )
        passed = result == test["expected"]

        print(f"Test {i}:")
        print(
            f"  Panels: {test['panel_w']}x{test['panel_h']}, "
            f"Roof: {test['roof_w']}x{test['roof_h']}"
        )
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    run_tests()
    print("🐕 Wuuf wuuf wuuf  Con bonus! 🐕")
    print("================================\n")
    run_tests_overlap()


if __name__ == "__main__":
    main()
