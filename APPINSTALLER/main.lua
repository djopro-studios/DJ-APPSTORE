local gui = require('paxolib')

function run()

	
    local window = gui.window("APPinstaller")
	local title = gui.label(window, 60, 50, 200, 100)
	local connect = gui.button(window, 60, 120, 200, 50)
    local code = gui.label(window, 60, 180, 200, 50)
	local APPinfo = gui.label(window, 60, 180, 250, 160)
	local install = gui.button(window, 60, 350, 200, 50)

	local codeLink = ""
	local name = ""
	local version = ""
	local desc = ""

	local clicked = 0 -- times of clicked in the connect button

	local OUT = "" -- THIS VALUE IS USED TO GET THE OUTPUT KEYBOARD

	local function DJKeyboard(win,visible,type,valueDONEKEYBOARD)
		local tall = 405

		local b_1 = gui.label(win, 0, tall, 30, 40)
        local b_2 = gui.label(win, 30, tall, 30, 40)
        local b_3 = gui.label(win, 60, tall, 30, 40)
        local b_4 = gui.label(win, 90, tall, 30, 40)
        local b_5 = gui.label(win, 120, tall, 30, 40)
        local b_6 = gui.label(win, 150, tall, 30, 40)
        local b_7 = gui.label(win, 185, tall, 30, 40)
        local b_8 = gui.label(win, 220, tall, 30, 40)
        local b_9 = gui.label(win, 250, tall, 30, 40)
        local b_0 = gui.label(win, 280, tall, 30, 40)

		local erase = gui.image(win,"KB_files/backspace.png", 0, 430, 50, 50)
        local enter = gui.image(win,"KB_files/enter.png", 260, 430, 40, 50)
		local labelKEY = gui.label(win,50,440,220,40)

		local keys = {
			{b_1, "1"}, {b_2, "2"}, {b_3, "3"}, {b_4, "4"}, {b_5, "5"},
			{b_6, "6"}, {b_7, "7"}, {b_8, "8"}, {b_9, "9"}, {b_0, "0"}
			-- Add d_3 and d_fin if needed
			}

			for _, keyInfo in ipairs(keys) do
				local button, text = keyInfo[1], keyInfo[2]
				button:setText(text)
			end

			

			local buttons = {b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, b_0}

			local function handleButtonClick(button)
				local key = button:getText()
			 	OUT = OUT .. key
				labelKEY:setText(OUT)
				print(OUT)
			end
            -- Attach the common function to each button
            for _, button in ipairs(buttons) do
                button:onClick(function()
                    
                    
                    handleButtonClick(button)

                end)
            end

            enter:onClick(function()
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
                labelKEY:setText(OUT)
                print(OUT)
            end)
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
		
		print(clicked)
		if clicked == 0 then
			print("bonjour -------")
			DJKeyboard(window,"SHOW","number",function() 
				   print("code" .. OUT)
					name = HTTP("http://45.90.13.219:6109/paxo/"..OUT.."/name.txt")
					version = HTTP("http://45.90.13.219:6109/paxo/"..OUT.."/version.txt")
					desc = HTTP("http://45.90.13.219:6109/paxo/"..OUT.."/des.txt")
	
					codeLink = OUT
					code:setText("Code : ".. OUT)
					local info = "App Name : "..name.."\n".."Version : "..version.."\n".. "Description : "..desc.."\n"
					APPinfo:setText(info)
	
		   end)
		end
		clicked = clicked + 1
	end)
	
	

	install:onClick(function()
		local mainFile = HTTP("http://45.90.13.219:6109/paxo/"..codeLink.."/main.lua")
		local confFile = HTTP("http://45.90.13.219:6109/paxo/"..codeLink.."/conf.txt")
		local imgFile = HTTP("http://45.90.13.219:6109/paxo/"..codeLink.."/logo.txt")
		local folder  = "../"..name
		
		gui.newDir(folder)
		gui.writeFile(folder.."/main.lua", mainFile)
		gui.writeFile(folder.."/conf.txt", confFile)
		gui.writeFile(folder.."/logo.png", tostring(imgFile))
		install:setColor(gui.COLOR_SUCCESS)
	end)
	
		

	
	

end
