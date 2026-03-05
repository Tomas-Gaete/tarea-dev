import * as fs from "fs";
import { totalmem } from "os";
import { json } from "stream/consumers";

interface TestCase {
	panelW: number;
	panelH: number;
	roofW: number;
	roofH: number;
	expected: number;
}
interface TestCaseOverlap {
	panelW: number;
	panelH: number;
	roofW: number;
	roofH: number;
	overlap:overlap_dict;
	expected: number;
}

interface TestData {
	testCases: TestCase[];
}

interface TestDataOverlap {
	testCases: TestCaseOverlap[];
}
function check_panel_dimensions(
	panelWidth: number,
	panelHeight: number,
	roofWidth: number,
	roofHeight: number,
) {
	var result: boolean;

	result = true;
	if (roofWidth < panelWidth || roofHeight < panelHeight) {
		result = false;
	}

	return result;
}
function calculatePanels(
	panelWidth: number,
	panelHeight: number,
	roofWidth: number,
	roofHeight: number,
): number {
	// Implementa acá tu solución
	//Cree la funcion check_panel_dimensions arriba para dejar ordenado el código
	//Cree aparte la función calculatePanels_overlap para el desafío opcional 2
	var roofArea: number = roofWidth * roofHeight;
	var panelArea: number = panelWidth * panelHeight;
	var fits: boolean;
	var fitsRotated: boolean;
	var result: number;

	fits = check_panel_dimensions(panelWidth, panelHeight, roofWidth, roofHeight);
	fitsRotated = check_panel_dimensions(
		panelHeight,
		panelWidth,
		roofWidth,
		roofHeight,
	);
	result = fits || fitsRotated ? Math.floor(roofArea / panelArea) : 0;
	return result;
}
class overlap_dict {
	"width": number;
	"height": number;
}

function calculatePanels_overlap(
	panelWidth: number,
	panelHeight: number,
	roofWidth: number,
	roofHeight: number,
	overlap: overlap_dict,
): number {
	// Implementa acá tu solución
	
	var overlap: overlap_dict = overlap;
	var overlapArea: number = overlap.width * overlap.height
	var TotalRoofArea: number = roofWidth * roofHeight*2 - overlapArea;
	var panelArea: number = panelWidth * panelHeight;
	var fits: boolean;
	var fitsRotated: boolean;
	var result: number;

	fits = check_panel_dimensions(panelWidth, panelHeight, roofWidth, roofHeight);
	fitsRotated = check_panel_dimensions(
		panelHeight,
		panelWidth,
		roofWidth,
		roofHeight,
	);
	result = fits || fitsRotated ? Math.floor(TotalRoofArea / panelArea) : 0;

	return result;
}

function main(): void {
	console.log("🐕 Wuuf wuuf wuuf 🐕");
	console.log("================================\n");

	runTests();
	console.log("🐕 Wuuf wuuf wuuf con bonus! 🐕");
	console.log("================================\n");
	runTestsOverlap();
}

function runTests(): void {
	const data: TestData = JSON.parse(
		fs.readFileSync("test_cases.json", "utf-8"),
	);
	const testCases = data.testCases;

	console.log("Corriendo tests:");
	console.log("-------------------");

	testCases.forEach((test: TestCase, index: number) => {
		const result = calculatePanels(
			test.panelW,
			test.panelH,
			test.roofW,
			test.roofH,
		);
		const passed = result === test.expected;

		console.log(`Test ${index + 1}:`);
		console.log(
			`  Panels: ${test.panelW}x${test.panelH}, Roof: ${test.roofW}x${test.roofH}`,
		);
		console.log(`  Expected: ${test.expected}, Got: ${result}`);
		console.log(`  Status: ${passed ? "✅ PASSED" : "❌ FAILED"}\n`);
	});
}

function runTestsOverlap(): void {
	const data: TestDataOverlap = JSON.parse(
		fs.readFileSync("test_cases_overlap.json", "utf-8"),
	);
	const testCases = data.testCases;

	console.log("Corriendo tests con bonificación 2:");
	console.log("-------------------");

	testCases.forEach((test: TestCaseOverlap, index: number) => {
		const result = calculatePanels_overlap(
			test.panelW,
			test.panelH,
			test.roofW,
			test.roofH,
			test.overlap
		);
		const passed = result === test.expected;

		console.log(`Test ${index + 1}:`);
		console.log(
			`  Panels: ${test.panelW}x${test.panelH}, Roof: ${test.roofW}x${test.roofH}`,
		);
		console.log(`  Expected: ${test.expected}, Got: ${result}`);
		console.log(`  Status: ${passed ? "✅ PASSED" : "❌ FAILED"}\n`);
	});
}

main();
