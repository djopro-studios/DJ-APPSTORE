local gui = require('paxolib')

function run()

	
    local window = gui.window("APPinstaller")
	local title = gui.label(window, 60, 50, 200, 100)
	local connect = gui.button(window, 60, 120, 200, 50)
    local code = gui.label(window, 60, 180, 200, 50)
	local APPinfo = gui.label(window, 60, 180, 250, 200)
	local install = gui.button(window, 60, 350, 200, 50)

	local codeLink = ""
	local name = ""
	local version = ""
	local desc = ""

	local OUT = "" -- THIS VALUE IS USED TO GET THE OUTPUT KEYBOARD

	function DJKeyboard(windowPrece,shHide,TypeKeyboard,valueDONEKEYBOARD)
			local gui = require('paxolib')
			local default = ""
			local LIVEtext = false
			local specialKeys = "yes"
	
			function LIVEtext_LABEL()  end
			
		
			
			-- shHide = SHOW / HIDE
			-- windowPrece = WINDOW THAT TO BE BASCULATE
			
		if TypeKeyboard == "string" then
			if shHide == "SHOW" then
		
				local OUTKeyboard = ""
			
				local KEYBOARD = gui.window("Keyboard")
				
				default = ""
				local currentKey = "DJ_Keyboard.txt"
				local title = gui.label(KEYBOARD, 60, 50, 200, 100)
			
				KEYBOARD:setWidth(350)
				KEYBOARD:setHeight(185)
				KEYBOARD:setX(0)
				KEYBOARD:setY(295)
			
			
				-- LINE 1 || 290
				local a_1 = gui.label(KEYBOARD, 0, 0, 30, 40)
				local a_2 = gui.label(KEYBOARD, 30, 0, 30, 40)
				local a_3 = gui.label(KEYBOARD, 60, 0, 30, 40)
				local a_4 = gui.label(KEYBOARD, 90, 0, 30, 40)
				local a_5 = gui.label(KEYBOARD, 120, 0, 30, 40)
				local a_6 = gui.label(KEYBOARD, 150, 0, 30, 40)
				local a_7 = gui.label(KEYBOARD, 185, 0, 30, 40)
				local a_8 = gui.label(KEYBOARD, 220, 0, 30, 40)
				local a_9 = gui.label(KEYBOARD, 250, 0, 30, 40)
				local a_10 = gui.label(KEYBOARD, 280, 0, 30, 40)
			
				-- LINE 2 || 335
			
				local b_1 = gui.label(KEYBOARD, 0, 40, 30, 40)
				local b_2 = gui.label(KEYBOARD, 30, 40, 30, 40)
				local b_3 = gui.label(KEYBOARD, 60, 40, 30, 40)
				local b_4 = gui.label(KEYBOARD, 90, 40, 30, 40)
				local b_5 = gui.label(KEYBOARD, 120, 40, 30, 40)
				local b_6 = gui.label(KEYBOARD, 150, 40, 30, 40)
				local b_7 = gui.label(KEYBOARD, 185, 40, 30, 40)
				local b_8 = gui.label(KEYBOARD, 220, 40, 30, 40)
				local b_9 = gui.label(KEYBOARD, 250, 40, 30, 40)
				local b_10 = gui.label(KEYBOARD, 280, 40, 30, 40)
			
				-- LINE 3 || 380
			
				local c_maj = gui.label(KEYBOARD, 0, 80, 50, 40)
				local c_2 = gui.label(KEYBOARD, 50, 80, 30, 40)
				local c_3 = gui.label(KEYBOARD, 90, 80, 30, 40)
				local c_4 = gui.label(KEYBOARD, 125, 80, 30, 40)
				local c_5 = gui.label(KEYBOARD, 160, 80, 30, 40)
				local c_6 = gui.label(KEYBOARD, 195, 80, 30, 40)
				local c_7 = gui.label(KEYBOARD, 230, 80, 30, 40)
				local c_del = gui.image(KEYBOARD, "KB_files/backspace.png", 265, 80, 45, 40)
				
				-- LINE 4 || 425
			
				local d_spe = gui.label(KEYBOARD, 0, 130, 50, 40)
				local d_2 = gui.image(KEYBOARD, "KB_files/lang.png", 55, 140, 25, 25)
				local d_3 = gui.image(KEYBOARD, "KB_files/space.png", 90, 130, 135, 40)
				local d_4 = gui.label(KEYBOARD, 230, 130, 30, 40)
				local d_fin = gui.image(KEYBOARD, "KB_files/enter.png", 265, 130, 45, 40)
				
				
	
				gui.setWindow(KEYBOARD)
				
				local AZQWER = ""
		
				local function setKeysLOCAL(name,TYPE,specialKey)
					
					if specialKey == "yes" then
	
						-- VALUE SPECIALKEYS
						
						-- CHANGE BUTTON DISPLAY
					
	
						local keys = {
							{a_1, "1"}, {a_2, "2"}, {a_3, "3"}, {a_4, "4"}, {a_5, "5"},
							{a_6, "6"}, {a_7, "7"}, {a_8, "8"}, {a_9, "9"}, {a_10, "0"},
							{b_1, "'"}, {b_2, "-"}, {b_3, "/"}, {b_4, "{"}, {b_5, "}"},
							{b_6, "<"}, {b_7, ">"}, {b_8, "."}, {b_9, "&"}, {b_10, "#"},
							{c_maj, "@"}, {c_2, "~"}, {c_3, "("}, {c_4, ")"}, {c_5, ":"},
							{c_6, ";"}, {c_7, "_"},
							{d_spe, "ABC"},
							{d_4, "?"}
							-- Add d_fin:setText("DONE") if needed
						}
	
							for _, keyInfo in ipairs(keys) do
								local button, text = keyInfo[1], keyInfo[2]
									button:setText(text)
								 -- Optional: Set font size for specific buttons
								if button == c_maj or button == d_spe then
									 button:setFontSize(15)
								end
							end
					
						
					end
	
					if name == "AZERTY" then
		
						AZQWER = "AZERTY"
						if TYPE == "MIN" then
		
							local keys = {
							{a_1, "a"}, {a_2, "z"}, {a_3, "e"}, {a_4, "r"}, {a_5, "t"},
							{a_6, "y"}, {a_7, "u"}, {a_8, "i"}, {a_9, "o"}, {a_10, "p"},
							{b_1, "q"}, {b_2, "s"}, {b_3, "d"}, {b_4, "f"}, {b_5, "g"},
							{b_6, "h"}, {b_7, "j"}, {b_8, "k"}, {b_9, "l"}, {b_10, "m"},
							{c_maj, "min"}, {c_2, "w"}, {c_3, "x"}, {c_4, "c"}, {c_5, "v"},
							{c_6, "b"}, {c_7, "n"},
							{d_spe, ";:!"},
							{d_4, ","}
							-- Add d_3 and d_fin if needed
							}
	
							for _, keyInfo in ipairs(keys) do
								local button, text = keyInfo[1], keyInfo[2]
								button:setText(text)
	
								-- Optional: Set font size for specific buttons
								if button == c_maj or button == d_spe then
									button:setFontSize(15)
								end
							end
	
		
						else
		
							local buttonTextMappings = {
								{a_1, "A"}, {a_2, "Z"}, {a_3, "E"}, {a_4, "R"}, {a_5, "T"},
								{a_6, "Y"}, {a_7, "U"}, {a_8, "I"}, {a_9, "O"}, {a_10, "P"},
								{b_1, "Q"}, {b_2, "S"}, {b_3, "D"}, {b_4, "F"}, {b_5, "G"},
								{b_6, "H"}, {b_7, "J"}, {b_8, "K"}, {b_9, "L"}, {b_10, "M"},
								{c_maj, "MAJ"}, {c_2, "W"}, {c_3, "X"}, {c_4, "C"}, {c_5, "V"},
								{c_6, "B"}, {c_7, "N"},
								{d_spe, "(-:"},
								{d_4, "'"}
								-- Add d_3 and d_fin if needed
							}
							
							for _, mapping in ipairs(buttonTextMappings) do
								local button, text = mapping[1], mapping[2]
								button:setText(text)
							
								-- Optional: Set font size for specific buttons
								if button == c_maj or button == d_spe then
									button:setFontSize(15)
								end
							end
							
		
						end
					end
		
					if name == "QWERTY" then
		
						AZQWER = "QWERTY"
						if TYPE == "MIN" then
		
							local buttonTextMappings = {
								{a_1, "q"}, {a_2, "w"}, {a_3, "e"}, {a_4, "r"}, {a_5, "t"},
								{a_6, "y"}, {a_7, "u"}, {a_8, "i"}, {a_9, "o"}, {a_10, "p"},
								{b_1, "a"}, {b_2, "s"}, {b_3, "d"}, {b_4, "f"}, {b_5, "g"},
								{b_6, "h"}, {b_7, "j"}, {b_8, "k"}, {b_9, "l"}, {b_10, "z"},
								{c_maj, "min"}, {c_2, "x"}, {c_3, "c"}, {c_4, "v"}, {c_5, "b"},
								{c_6, "n"}, {c_7, "m"},
								{d_spe, ";:!"},
								{d_4, ","}
								-- Add d_3 and d_fin if needed
							}
							
							for _, mapping in ipairs(buttonTextMappings) do
								local button, text = mapping[1], mapping[2]
								button:setText(text)
							
								-- Optional: Set font size for specific buttons
								if button == c_maj or button == d_spe then
									button:setFontSize(15)
								end
							end
							
		
						else
		
							local buttonLabelMappings = {
								{a_1, "Q"}, {a_2, "W"}, {a_3, "E"}, {a_4, "R"}, {a_5, "T"},
								{a_6, "Y"}, {a_7, "U"}, {a_8, "I"}, {a_9, "O"}, {a_10, "P"},
								{b_1, "A"}, {b_2, "S"}, {b_3, "D"}, {b_4, "F"}, {b_5, "G"},
								{b_6, "H"}, {b_7, "J"}, {b_8, "K"}, {b_9, "L"}, {b_10, "Z"},
								{c_maj, "MAJ"}, {c_2, "X"}, {c_3, "C"}, {c_4, "V"}, {c_5, "B"},
								{c_6, "N"}, {c_7, "M"},
								{d_spe, ")-:"},
								{d_4, ","}
							}
							
							for _, mapping in ipairs(buttonLabelMappings) do
								local button, label = mapping[1], mapping[2]
								button:setText(label)
							
								-- Optional: Set font size for specific buttons
								if button == c_maj or button == d_spe then
									button:setFontSize(15)
								end
							end
							
		
						end
					end
	
					
			
				end
				local typeMINMAJ = "MIN"
				function getLine(text, lineNumber)
					local currentLine = 0
				
					for line in text:gmatch("([^\r\n]*)[\r\n]?") do
						currentLine = currentLine + 1
						function isEven(number)
							return number % 2 == 0
						end
			
						if isEven(lineNumber) then
							lineNumber = lineNumber + 1
						else
							--print("-----------------   nothing")
						end
	
						if currentLine == lineNumber then
							return line
						end
					end
				
					-- If the requested line number is out of range, return nil
					return nil
				end
			
				local fileKeyDEFAULT = getLine(gui.readFile("default.txt"),1)
				
				--print("-------------------    " .. fileKeyDEFAULT)
		
				
				if fileKeyDEFAULT == "AZERTY" then
					setKeysLOCAL("AZERTY","MIN","no")
				else
					setKeysLOCAL("QWERTY","MIN","no")
				end
			
				local function setKeyboard()
					local window1 = gui.window("Keyboard Switch")
					local up = gui.button(window1, 230, 110, 60, 60) 
					local down = gui.button(window1, 230, 40, 60, 60)
					local keyboardSelect = gui.label(window1, 20, 70, 200, 50) 
					local done = gui.button(window1, 15, 130, 200, 40) 
					--local done1 = gui.button(window1, 125, 420, 100, 40)
			
					window1:setWidth(350)
					window1:setHeight(185)
					window1:setX(0)
					window1:setY(295)
					
					gui.setWindow(window1)
					done:setText("Select")
					up:setText("/\\")
					down:setText("\\/")
					local list = 1
					local ifFile = true
					if ifFile then
						
						AZQWER = "AZERTY"
						local name = "AZERTY"
						keyboardSelect:setText(name)
	
					else
			
						keyboardSelect:setText(" NO KEYBOARD DETECTED")
					end
			
					up:onClick( function()
						
						list = list + 1
						local ifFile = true
						if ifFile then
							
							AZQWER = "QWERTY"
							local name = "QWERTY"
							keyboardSelect:setText(name)
				
						else
				
							keyboardSelect:setText(" NO KEYBOARD DETECTED")
						end
					end)
			
					down:onClick( function()
						
						list = list - 1
						local ifFile = true
						if ifFile then
							
							AZQWER = "AZERTY"
							local name = "AZERTY"
							keyboardSelect:setText(name)
				
						else
				
							keyboardSelect:setText(" NO KEYBOARD DETECTED")
						end
					end)
			
					done:onClick( function()
						local ifFile = true
						if ifFile then
							
							gui.writeFile("default.txt", tostring(AZQWER))
							if AZQWER == "AZERTY" then
								setKeysLOCAL("AZERTY","MIN","no")
							else
								setKeysLOCAL("QWERTY","MIN","no")
							end
	
							gui.setWindow(KEYBOARD)
	
							-- SHOW THE ICONS
							c_del = gui.image(KEYBOARD, "KB_files/backspace.png", 265, 80, 45, 40)
							d_2 = gui.image(KEYBOARD, "KB_files/lang.png", 55, 140, 25, 25)
							d_3 = gui.image(KEYBOARD, "KB_files/space.png", 90, 130, 135, 40)
							d_fin = gui.image(KEYBOARD, "KB_files/enter.png", 265, 130, 45, 40)
	
						end
			
					end)
					
				end
			
				d_2:onClick( function()
					setKeyboard()
				end)
	
				-- Common function for button click event
				local function handleButtonClick(button)
						local key = button:getText()
					 OUT = OUT .. key
					if LIVEtext then
						LIVEtext_LABEL()
					end
					print(OUT)
				end
				
				-- List of buttons
				local buttons = {a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, b_10, c_2, c_3, c_4, c_5, c_6, c_7}
	
				-- Attach the common function to each button
				for _, button in ipairs(buttons) do
					button:onClick(function()
						
						
						handleButtonClick(button)
	
					end)
				end
	
				c_del:onClick( function()
					function removeOneChar(inputString)
						if #inputString > 0 then
							return string.sub(inputString, 1, -2)  -- Removes the last character
						else
							return inputString  -- String is empty, nothing to remove
						end
					end
					local key = removeOneChar(OUT)
					--OUTKeyboard = key
					OUT = key
					if LIVEtext then
						LIVEtext_LABEL()
					end
					print(OUT)
				end)
		
				c_maj:onClick( function()
	
					if specialKeys == "yes" then
	
						if typeMINMAJ == "MIN" then
							setKeysLOCAL(AZQWER,"MAJ","no")
							typeMINMAJ = "MAJ"
						else
							setKeysLOCAL(AZQWER,"MIN","no")
							typeMINMAJ = "MIN"
						end
	
					else
	
						local key = OUT .."@"
					
						OUT = key
						--OUT = OUTKeyboard
						if LIVEtext then
							LIVEtext_LABEL()
						end
						print(OUT)
	
					end
	
					
				end)
			
				d_3:onClick( function()
					local key = OUT .. " "
					
					
					OUT = key
					if LIVEtext then
						LIVEtext_LABEL()
					end
					print(OUT)
				end)
		
				d_fin:onClick(function()
					gui.setWindow(windowPrece)
					valueDONEKEYBOARD()
				end)
	
				d_spe:onClick(function()
					
					if specialKeys == "yes" then
						setKeysLOCAL("none","MIN","yes")
						specialKeys = "no"
						print("SPECIALKEYS ----  : " .. tostring(specialKeys))
					else
	
						setKeysLOCAL(AZQWER,"MIN","no")
						specialKeys = "yes"
						print("SPECIALKEYS ----  : " .. tostring(specialKeys))
	
					end
					
					
				end)
		
			else
				gui.setWindow(windowPrece)
			end
		elseif TypeKeyboard == "number" then
				local OUTKeyboard = ""
			
				local KEYBOARD = gui.window("Number")
				
				default = ""
				
				local title = gui.label(KEYBOARD, 60, 50, 200, 100)
			
				KEYBOARD:setWidth(350)
				KEYBOARD:setHeight(185)
				KEYBOARD:setX(0)
				KEYBOARD:setY(295)
			
			
				-- LINE 1 || 290
				local a_1 = gui.label(KEYBOARD, 80, 10, 40, 50)
				local a_2 = gui.label(KEYBOARD, 140, 10, 40, 50)
				local a_3 = gui.label(KEYBOARD, 200, 10, 40, 50)
	
				local a_4 = gui.label(KEYBOARD, 80, 52, 40, 50)
				local a_5 = gui.label(KEYBOARD, 140, 52, 40, 50)
				local a_6 = gui.label(KEYBOARD, 200, 52, 40, 50)
	
				local a_7 = gui.label(KEYBOARD, 80, 92, 40, 50)
				local a_8 = gui.label(KEYBOARD, 140, 92, 40, 50)
				local a_9 = gui.label(KEYBOARD, 200, 92, 40, 50)
	
				local erase = gui.image(KEYBOARD,"KB_files/backspace.png", 70, 122, 50, 50)
				local a_10 = gui.label(KEYBOARD, 140, 132, 40, 50)
				local enter = gui.image(KEYBOARD,"KB_files/enter.png", 200, 122, 40, 50)
	
				
				gui.setWindow(KEYBOARD)
	
				local keys = {
					{a_1, "1"}, {a_2, "2"}, {a_3, "3"}, {a_4, "4"}, {a_5, "5"}, {a_6, "6"}, {a_7, "7"}, {a_8, "8"}, {a_9, "9"}, {a_10, "0"}
					-- Add d_3 and d_fin if needed
				}
	
					for _, keyInfo in ipairs(keys) do
						local button, text = keyInfo[1], keyInfo[2]
						button:setFontSize(25)
						button:setText(text)
	
						-- Optional: Set font size for specific buttons
						
					end
	
				local function handleButtonClick(button)
						local key = button:getText()
					 OUT = OUT .. key
					if LIVEtext then
						LIVEtext_LABEL()
					end
					print(OUT)
				end
				
				-- List of buttons
				local buttons = {a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10}
	
				-- Attach the common function to each button
				for _, button in ipairs(buttons) do
					button:onClick(function()
						
						
						handleButtonClick(button)
	
					end)
				end
	
				enter:onClick(function()
					gui.setWindow(windowPrece)
					valueDONEKEYBOARD()
				end)
	
				erase:onClick( function()
					function removeOneChar(inputString)
						if #inputString > 0 then
							return string.sub(inputString, 1, -2)  -- Removes the last character
						else
							return inputString  -- String is empty, nothing to remove
						end
					end
					local key = removeOneChar(OUT)
					--OUTKeyboard = key
					OUT = key
					if LIVEtext then
						LIVEtext_LABEL()
					end
					print(OUT)
				end)
	
		end
	end
	
	-- GETWEB SYSTEM || GET DATA FROM FILE IN THE WEB
	local function HTTP(URL)
		local reponce = gui.getWeb(URL)
		return reponce
	end
	-- EXAMPLE || print(tostring(HTTP("http://192.168.56.1/text.txt")))
	
	gui.setWindow(window)
	


	title:setText("APP INSTALLER")
	connect:setText("Connect")
	code:setText("")
	install:setText("Install Now")
	connect:onClick(function()
		print("bonjour -------")
		DJKeyboard(window,"SHOW","number",function() 
			   print("code" .. OUT)
				name = HTTP("http://45.90.13.218:6109/paxo/"..OUT.."/name.txt")
				version = HTTP("http://45.90.13.218:6109/paxo/"..OUT.."/version.txt")
				desc = HTTP("http://45.90.13.218:6109/paxo/"..OUT.."/des.txt")

				codeLink = OUT
				code:setText("Code : ".. OUT)
				local info = "App Name : "..name.."\n".."Version : "..version.."\n".. "Description : "..desc.."\n"
				APPinfo:setText(info)

	   end)
	end)
	
	

	install:onClick(function()
		local mainFile = HTTP("http://45.90.13.218:6109/paxo/"..codeLink.."/main.lua")
		local confFile = HTTP("http://45.90.13.218:6109/paxo/"..codeLink.."/conf.txt")
		local imgFile = HTTP("http://45.90.13.218:6109/paxo/"..codeLink.."/logo.txt")
		local folder  = "../"..name
		
		gui.newDir(folder)
		gui.writeFile(folder.."/main.lua", mainFile)
		gui.writeFile(folder.."/conf.txt", confFile)
		gui.writeFile(folder.."/logo.png", tostring(imgFile))
		install:setColor(gui.COLOR_SUCCESS)
	end)
	
		

	
	

end