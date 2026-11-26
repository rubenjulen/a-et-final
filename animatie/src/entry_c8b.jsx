import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { Clip8b } from './Clip8b';
import t from './timing_c8b.json';

const FPS = 30;
const Root = () => (<>
  <Composition id="Clip8b" component={Clip8b} durationInFrames={Math.ceil(t.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
